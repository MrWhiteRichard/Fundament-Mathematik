using Plots

struct maze
    states
    start
    goal
    actions
    gamma
end


# Define the maze

states = vec([(x,y) for x in 1:9, y in 1:6])
obstacles = [(3,3), (3,4), (3,5), (6,2), (8,4), (8,5), (8,6)]
filter!(e-> e ∉ obstacles, states)
start = (1,4)
goal = (9,6)
actions = [(-1,0),(1,0),(0,-1),(0,1)]
gamma = 0.95

test_maze = maze(states, start, goal, actions, gamma)


function transition(maze, current_state, current_action)
    if current_state .+ current_action ∈ maze.states
        next_state = current_state .+ current_action
    else
        next_state = current_state
    end
    if next_state == goal
        next_reward = 1
    else
        next_reward = 0
    end
    return next_state, next_reward
end

function epsilon_greedy_policy(Q, current_state, maze, epsilon)
    if rand() < epsilon
        action = rand(maze.actions)
    else
        best_actions = []
        max_Qvalue = maximum([Q[(current_state, action)] for action in maze.actions])
        for action in maze.actions
            if Q[(current_state, action)] == max_Qvalue
                push!(best_actions, action)
            end
        end
        action = rand(best_actions)
    end

    return action

end

function tabular_dynaQ(maze, n, max_episodes, epsilon, alpha)
    # Initialization

    Q = Dict((state, action) => 0.0 for state in maze.states, action in maze.actions )
    Model = Dict()

    episode_counter = 0
    steps_per_episode = Vector{Int64}()

    while episode_counter < max_episodes
        episode_counter += 1
        current_state = maze.start
        next_state = maze.start
        step_counter = 0

        while current_state != goal
            step_counter += 1
            current_state = next_state
            current_action = epsilon_greedy_policy(Q, current_state, maze, epsilon)
            next_state, next_reward = transition(maze, current_state, current_action)
            Q[(current_state, current_action)] += alpha*(next_reward + maze.gamma*maximum([Q[(next_state, action)] for action in maze.actions]) - Q[(current_state, current_action)])
            Model[(current_state, current_action)] = (next_state, next_reward)
            for i in 1:n
                random_state, random_action = rand(keys(Model))
                model_next_state, model_next_reward = Model[(random_state, random_action)]
                Q[(random_state, random_action)] += alpha*(model_next_reward + maze.gamma*maximum([Q[(model_next_state, action)] for action in maze.actions]) - Q[(random_state, random_action)])
            end
        end
        push!(steps_per_episode, step_counter)
    end
    return Q, steps_per_episode
end

function multi_step_method(environment, n, max_episodes, epsilon, alpha)
    Q = Dict((state, action) => 0.0 for state in environment.states, action in environment.actions )
    

    episode_counter = 0
    steps_per_episode = []
    while episode_counter < max_episodes
        episode_counter += 1

        state_array = Array{Any}(undef, n+1)
        action_array = Array{Any}(undef, n+1)
        reward_array = Array{Float64}(undef, n+1)

        current_state = environment.start
        current_action = epsilon_greedy_policy(Q, current_state, environment, epsilon)

        state_array[1] = current_state
        action_array[1] = current_action
        t = 0
        T = Inf
        tau = -Inf
        while tau < T - 1
            t = t+1
            if T == Inf
                current_state, current_reward = transition(environment, current_state, current_action)
                state_array[t%(n+1)+1] = current_state
                reward_array[t%(n+1)+1] = current_reward
                if current_state == environment.goal
                    T = t
                else
                    current_action = epsilon_greedy_policy(Q, current_state, environment, epsilon)
                    action_array[t%(n+1)+1] = current_action
                end
            end

            tau = t - n
            if tau >= 0
                G = 0
                for i in tau+1:trunc(Int, min(tau+n,T))
                    G += environment.gamma^(i - tau - 1)*reward_array[i%(n+1)+1]
                end
                if tau + n < T
                    G += environment.gamma^n*Q[(state_array[(tau+n)%(n+1)+1], action_array[(tau+n)%(n+1)+1])]
                end
                Q[(state_array[tau%(n+1) + 1], action_array[tau%(n+1)+1])] += alpha*(G - Q[(state_array[tau%(n+1) + 1], action_array[tau%(n+1)+1])])
            end

        end
        push!(steps_per_episode, T)
    end
    return Q, steps_per_episode
end

# Parameter
epsilon = 0.1
alpha = 0.1
max_episodes = 50
n_array = [0,5,50]


fig1 = plot(xlabel = "Episode", ylabel = "Steps per Episode", title = "Tabular Dyna-Q with n planning steps")
for n in n_array
    Q1, step_counter1 = tabular_dynaQ(test_maze, n, max_episodes, epsilon, alpha)
    plot!(fig1, 2:length(step_counter1), step_counter1[2:end], label = "Dyna-Q: n = $n")
    
end

#png(fig1, "SS_2021/ReiL_UE/Übung_4/Florian/6.3.1")

max_episodes = 50
repetitions = 100
avg_step_counter1 = zeros(max_episodes)
avg_step_counter2 = zeros(max_episodes)
fig2 = plot(xlabel = "Episode", ylabel = "Steps per Episode (averaged over 100 repetitions)", title = "Tabular Dyna-Q vs. SARSA", yaxis = :log)

linestyles = [:solid, :dash, :dot]
for (n, lty) in zip([5,10,50],linestyles)
    for j in 1:repetitions
        Q1, step_counter1 = tabular_dynaQ(test_maze, n, max_episodes, epsilon, alpha)
        Q2, step_counter2 = multi_step_method(test_maze, n, max_episodes, epsilon, alpha)

        for i in 1:max_episodes
            avg_step_counter1[i] += 1/j*(step_counter1[i] - avg_step_counter1[i])
            avg_step_counter2[i] += 1/j*(step_counter2[i] - avg_step_counter2[i])
        end
    end
    plot!(fig2, avg_step_counter1, label = "Dyna-Q: n = $n", color = "blue", linestyle = lty)
    plot!(fig2, avg_step_counter2, label = "SARSA: n = $n", color = "orange", linestyle = lty)
end

png(fig2, "SS_2021/ReiL_UE/Übung_4/Florian/6.3.2")

fig2