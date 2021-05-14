using Plots

# Windy Gridworld Setup

grid = vec([[x,y] for x in 1:10, y in 1:7])

wind = [0,0,0,1,1,1,2,2,1,0]

start = [1,4]

goal = [8,4]

eight_actions = vec([[x,y] for x = -1:1, y = -1:1 if [x,y] != [0,0]])

nine_actions = vec([[x,y] for x = -1:1, y = -1:1])


function sarsa(states, wind, actions, start, goal, alpha, epsilon)
    Q = Dict([state,action] => 0.0 for state in states, action in actions)
    policy = Dict(state => rand(actions) for state in states)


    total_episode_length = 0
    avg_episode_length = 100
    episode_counter = 0
    episode_length_cumsum = [0]
    while avg_episode_length > 16 && total_episode_length < 1000000
        episode_counter += 1
        current_state = start
        if rand() < epsilon
            current_action = rand(actions)
        else
            current_action = policy[current_state]
        end
        current_wind = 0
        episode_length = 1
        while current_state != goal
            episode_length += 1
            current_wind = wind[current_state[1]]

            

            new_state_x = max(1,min(10, current_state[1] + current_action[1]))
            new_state_y = max(1,min(7, current_state[2] + current_action[2] + current_wind))

            new_state = [new_state_x, new_state_y]

            if rand() < epsilon
                new_action = rand(actions)
            else
                new_action = policy[new_state]
            end


            Qmax = maximum([Q[[current_state,action]] for action in actions])

            Q[[current_state,current_action]] += alpha*(-1 + Q[[new_state, new_action]] - Q[[current_state, current_action]])

            if Q[[current_state,current_action]] > Qmax
                policy[current_state] = current_action
            end

            current_state = copy(new_state)
            current_action = copy(new_action) 
        end
        total_episode_length += episode_length
        push!(episode_length_cumsum, total_episode_length)
        avg_episode_length += (episode_length - avg_episode_length)/10
        if episode_counter%10 == 0
            println(avg_episode_length)
        end
    end
    return Q, policy, episode_length_cumsum
end

alpha = 0.5
epsilon = 0.1

Q, policy, episode_length_cumsum = sarsa(grid, wind, eight_actions, start, goal, alpha, epsilon)

plot(episode_length_cumsum, 1:length(episode_length_cumsum))

# for x in 1:10, y in 1:7
#     println("Q[",x,",",y,"][a] = ", [Q[[[x,y],a]] for a in eight_actions])
# end