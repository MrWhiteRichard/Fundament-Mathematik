using Plots

struct environment
    states
    start_states
    terminal_states
    actions
    gamma
end



function n_step_td_evaluation(policy; type, environment, alpha, n, number_of_episodes)
    state_values = Dict(state => 0.0 for state in environment.states)
    for state in environment.terminal_states
        state_values[state] = 0
    end
    mse_array = [sqrt(1/(k-2)*sum([(state_values[i] - i/(k-1))^2 for i in 1:(k-2)]))]
    episode_counter = 0
    while episode_counter < number_of_episodes
        episode_counter += 1

        state_array = Array{Any}(undef, n+1)
        reward_array = Array{Float64}(undef, n+1)
        error_array = Array{Float64}(undef, n+1)

        current_state = rand(environment.start_states)

        state_array[1] = current_state
        t = 0
        T = Inf
        tau = -Inf
        while tau < T - 1
            t = t+1
            if T == Inf
                current_action = rand(policy[current_state])
                current_state, current_reward = transition(environment, current_state, current_action)
                state_array[t%(n+1)+1] = current_state
                reward_array[t%(n+1)+1] = current_reward
                error_array[(t-1)%(n+1)+1] = current_reward + gamma*state_values[current_state] - state_values[state_array[(t-1)%(n+1)+1]]
                if current_state ∈ environment.terminal_states
                    T = t
                end
            end

            tau = t - n
            if tau >= 0
                G = 0
                if type == 1
                    for i in tau+1:trunc(Int, min(tau+n,T))
                        G += environment.gamma^(i - tau - 1)*reward_array[i%(n+1)+1]
                    end
                    if tau + n < T
                        G += environment.gamma^n*state_values[state_array[(tau+n)%(n+1)+1]]
                    end
                    state_values[state_array[tau%(n+1) + 1]] += alpha*(G - state_values[state_array[tau%(n+1) + 1]])
                elseif type == 2
                    for i in tau:trunc(Int, min(tau+n-1,T))
                        G += environment.gamma^(i - tau - 1)*error_array[i%(n+1)+1]
                    end
                    state_values[state_array[tau%(n+1) + 1]] += alpha*G
                end
                
            end

        end
        push!(mse_array, sqrt(1/k*sum([(state_values[i] - true_value_function[i])^2 for i in 1:k])))
    end
    return state_values, mse_array
end

# Environment: k-State Markov Reward Process (Example 6.2)
k = 19

states = collect(0:k+1)
start_states = collect(1:k)
terminal_states = [0,k+1]
gamma = 1
actions = [1]
true_value_function = Dict(i => (i-(k+1)/2)/((k+1)/2) for i in 1:k)
policy = Dict(i => 1 for i in 1:k)

function transition(environment, current_state, current_action)
    if rand() < 0.5
        next_state = current_state - 1
    else
        next_state = current_state + 1
    end
    if next_state == environment.terminal_states[2]
        reward = 1
    elseif next_state == environment.terminal_states[1]
        reward = -1
    else
        reward = 0
    end
    return next_state, reward
end

nineteen_state_mrp = environment(states, start_states, terminal_states, actions, gamma)
#state_values2, mse_array2 = n_step_td_evaluation(policy, type = 2, environment = nineteen_state_mrp, alpha = 0.5, n = 1, number_of_episodes = number_of_episodes)

number_of_episodes = 100

function plot_results()
    fig = plot(xlabel = "Number of Episodes", ylabel = "RMS error (averaged over 100 repetitions)", title = "$k-State MRP", legendfontsize= 6)
    linestyles = [:solid, :dash, :dot, :dashdot, :dashdotdot]
    for (n, linestyle) in zip([1,2,4,8,16],linestyles)
        alpha = min(0.9, round(1.4/n,digits=2))
        avg_mse_array1 = zeros(number_of_episodes)
        avg_mse_array2 = zeros(number_of_episodes)
        for j in 1:100
            state_values1, mse_array1 = n_step_td_evaluation(policy, type = 1, environment = nineteen_state_mrp, alpha = alpha, n = n, number_of_episodes = number_of_episodes)
            for i in 1:number_of_episodes
                avg_mse_array1[i] += 1/j*(mse_array1[i] - avg_mse_array1[i])
            end
            state_values2, mse_array2 = n_step_td_evaluation(policy, type = 2, environment = nineteen_state_mrp, alpha = alpha, n = n, number_of_episodes = number_of_episodes)
            for i in 1:number_of_episodes
                avg_mse_array2[i] += 1/j*(mse_array2[i] - avg_mse_array2[i])
            end
        end
        
        plot!(fig, avg_mse_array1, label = "Standard, n =  $n, alpha = $alpha", color = "blue", linestyle = linestyle)
        plot!(fig, avg_mse_array2, label = "Sum of TD, n = $n, alpha = $alpha", color = "red", linestyle = linestyle)
    end
    return fig
end

fig = plot_results()

png(fig, "SS_2021/ReiL_UE/Übung_4/Florian/6.2")

fig