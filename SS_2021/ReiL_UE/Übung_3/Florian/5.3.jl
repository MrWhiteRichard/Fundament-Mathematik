using Plots

# Windy Gridworld Setup

grid = vec([[x,y] for x in 1:10, y in 1:7])

deterministic_wind = [[0],[0],[0],[1],[1],[1],[2],[2],[1],[0]]

stochastic_wind = [[0],[0],[0],[0,1,2],[0,1,2],[0,1,2],[1,2,3],[1,2,3],[0,1,2],[0]]

start = [1,4]

goal = [8,4]

four_actions = [[0,1],[0,-1],[1,0],[-1,0]]

eight_actions = vec([[x,y] for x = -1:1, y = -1:1 if [x,y] != [0,0]])

nine_actions = vec([[x,y] for x = -1:1, y = -1:1])


function sarsa(states, wind, actions, start, goal, max_steps, alpha, epsilon)
    Q = Dict([state,action] => 0.0 for state in states, action in actions)
    policy = Dict(state => actions for state in states)


    total_episode_length = 0
    avg_episode_length = 100
    episode_counter = 0
    episode_length_cumsum = [0]
    while total_episode_length < max_steps
        episode_counter += 1
        current_state = start
        if rand() < epsilon
            current_action = rand(actions)
        else
            current_action = rand(policy[current_state])
        end
        current_wind = 0
        episode_length = 1
        while current_state != goal
            episode_length += 1
            current_wind = rand(wind[current_state[1]])
            new_state_x = max(1,min(10, current_state[1] + current_action[1]))
            new_state_y = max(1,min(7, current_state[2] + current_action[2] + current_wind))

            new_state = [new_state_x, new_state_y]

            if rand() < epsilon
                new_action = rand(actions)
            else
                new_action = rand(policy[new_state])
            end

            Q[[current_state,current_action]] += alpha*(-1 + Q[[new_state, new_action]] - Q[[current_state, current_action]])

            max_Qvalue = maximum([Q[[current_state, action]] for action in actions])
            best_actions = Vector{Vector{Int64}}()
            for action in actions
                if Q[[current_state, action]] == max_Qvalue
                    push!(best_actions, action)
                end
            end
            policy[current_state] = best_actions

            current_state = copy(new_state)
            current_action = copy(new_action) 
        end
        if episode_counter ==  1
            println("First episode length: ", episode_length)
        end
        total_episode_length += episode_length
        push!(episode_length_cumsum, total_episode_length)
        avg_episode_length += (episode_length - avg_episode_length)/10
    end
    println("Weighted average episode length: ", avg_episode_length)
    return Q, policy, episode_length_cumsum
end

# ToDo: Quiver-Plot of optimal policy

function plot_policy(start, fig, policy, wind, col)
    current_state = start

    plot!(fig, [1,10],[1,1], color = "black", label = "")
    plot!(fig, [1,10],[7,7], color = "black", label = "")
    plot!(fig, [1,1],[1,7], color = "black", label = "")
    plot!(fig, [10,10],[1,7], color = "black", label = "")


    i = 0
    while current_state != goal && i < 1000
        i += 1
        current_action = rand(policy[current_state])
        current_wind = rand(wind[current_state[1]])
        new_state_x = max(1,min(10, current_state[1] + current_action[1]))
        new_state_y = max(1,min(7, current_state[2] + current_action[2] + current_wind))

        new_state = [new_state_x, new_state_y]

        plot!(fig, [current_state[1], new_state_x], [current_state[2],new_state_y], 
            linetype= :steppre, arrow = true, label = "", color = col)

        current_state = copy(new_state)

    end
    println("Steps: ", i)
    #plot!(title = string(i)* " Steps")
end

alpha = 0.5
epsilon = 0.1

fig1 = plot(legend = :bottomright, palette = :Paired_12, title = "Deterministic Wind")
fig2 = plot(legend = :bottomright, palette = :Paired_12, title = "Stochastic Wind")
fig3 = plot(legend = :bottomright)

for (actions,col) in zip((four_actions, eight_actions, nine_actions),("red", "blue", "green"))

    println("Deterministic Wind, ", string(length(actions)) * " Actions")
    Q, policy, episode_length_cumsum = sarsa(grid, deterministic_wind, actions, start, goal, 20000, alpha, epsilon)

    plot!(fig1, episode_length_cumsum, 0:length(episode_length_cumsum)-1, label = string(length(actions)) * " Actions")

    plot_policy(start, fig3, policy, deterministic_wind, col)
    
    println("Stochastic Wind, ", string(length(actions)) * " Actions")
    Q, policy, episode_length_cumsum = sarsa(grid, stochastic_wind, actions, start, goal, 100000, alpha, epsilon)

    plot!(fig2, episode_length_cumsum, 0:length(episode_length_cumsum)-1, label = string(length(actions)) * " Actions")

end


display(fig1)

display(fig2)

display(fig3)

# for x in 1:10, y in 1:7
#     println("Q[",x,",",y,"][a] = ", [Q[[[x,y],a]] for a in eight_actions])
# end