# using Pkg
# Pkg.add("Plots")
# Pkg.add("BenchmarkTools")
# Pkg.add("PGFPlotsX")]

using Plots
using Random


### Racetrack-Configuration

struct RaceTrack
    xlims
    ylims
    velocity_limits
    start_states
    states
    finish_states
    goal_steps
end

## Simple Racetrack 1

xlims = vcat([(1,10) for i in 1:10],[(1,20) for i in 1:10])
ylims = [1,length(xlims)]

start_states = [[i,1,0,0] for i in 1:10]

velocity_limits = (0,2)

states = Vector{Vector{Int64}}()

for y in ylims[1]:ylims[2]
    for x in xlims[y][1]:xlims[y][2]
        for y_vel in velocity_limits[1]:velocity_limits[2]
            for x_vel in velocity_limits[1]:velocity_limits[2]
                push!(states,[x,y,x_vel,y_vel])
            end
        end
    end
end

finish_states = vec([[20,i,j,k] for i in 11:20, j in velocity_limits[1]:velocity_limits[2], k in velocity_limits[1]:velocity_limits[2]])

goal_steps = 15

race_track1 = RaceTrack(xlims, ylims, velocity_limits, start_states, states, finish_states, goal_steps)

## Intermediate Racetrack 2

xlims = vcat([(1,10) for i in 1:10],[(1+i,10+i) for i in 1:10],[(11+i,30) for i in 1:10])
ylims = [1,length(xlims)]

start_states = [[i,1,0,0] for i in 1:10]

velocity_limits = (0,5)

states = Vector{Vector{Int64}}()

for y in ylims[1]:ylims[2]
    for x in xlims[y][1]:xlims[y][2]
        for y_vel in velocity_limits[1]:velocity_limits[2]
            for x_vel in velocity_limits[1]:velocity_limits[2]
                push!(states,[x,y,x_vel,y_vel])
            end
        end
    end
end

finish_states = vec([[30,i,j,k] for i in 21:30, j in velocity_limits[1]:velocity_limits[2], k in velocity_limits[1]:velocity_limits[2]])

goal_steps = 30

race_track2 = RaceTrack(xlims, ylims, velocity_limits, start_states, states, finish_states, goal_steps)

### Actions

actions = vec([[x,y] for x = -1:1, y = -1:1])

### constant step-size Monte-Carlo-Algorithm

function monte_carlo(race_track, actions, epsilon, alpha, max_iterations)
    # Initialize action-value function 

    Q = Dict([state,action] => 0.0 for state in race_track.states, action in actions)

    # Start with random policy
    policy = Dict(state => [0,0] for state in race_track.states)
    
    avg_length = 1000
    i = 0
    while true
        i += 1
        start_state = rand(race_track.start_states)
        state_action_array = generate_episode(policy, epsilon/log(i+1), start_state, race_track.finish_states, race_track.ylims, race_track.velocity_limits)

        if state_action_array == "STOP"
            println("Warning: Maximum number of steps (100000) exceeded. Episode was discarded.")
            continue
        end

        policy, avg_length = improve_policy(policy, Q, state_action_array, alpha, avg_length, i)

        if (avg_length < race_track.goal_steps) || (i > max_iterations)
            break
        end

    end
    return Q, policy
end

function improve_policy(policy, Q, state_action_array, alpha, avg_length, i)
    
    returns = 0
    T = length(state_action_array)
    for t in (T-1):-1:1
        returns = returns - 1
        # if state_action_array[t] ∉ state_action_array[1:t-1]
            Q[state_action_array[t]] += (returns - Q[state_action_array[t]])*alpha


            # determine best action, with ties broken randomly
            max_Qvalue = maximum([Q[[state_action_array[t][1], action]] for action in actions])
            best_actions = Vector{Vector{Int64}}()
            for action in actions
                if Q[[state_action_array[t][1], action]] == max_Qvalue
                    push!(best_actions, action)
                end
            end
            policy[state_action_array[t][1]] = rand(best_actions)
        # end
    end
    avg_length += (length(state_action_array) - avg_length)*alpha

    if i%100 == 0
        println("Number of Iterations: ", i)
        println("Avg: ", avg_length, " Current: ", length(state_action_array))
    end
    
    return policy, avg_length
end

function generate_episode(policy, epsilon, start_state, finish_states, ylims, velocity_limits)
    current_state = start_state
    state_action_array = []

    n = 0

    while current_state ∉ finish_states
        n += 1
        new_state = copy(current_state)
        if rand() < epsilon
            next_action = rand(actions)
        else
            next_action = policy[current_state]
        end
        push!(state_action_array, [current_state, next_action])
        # Update velocity
        if rand() < 0.1
            next_action = [0,0]
        end
        for i in 3:4
            new_state[i] = min(velocity_limits[2],max(velocity_limits[1], new_state[i] + next_action[i-2]))
        end
        # No stopping on the track
        if new_state[3] == 0 && new_state[4] == 0
            new_state[3] = current_state[3]
            new_state[4] = current_state[4]
        end
        # Update position
        for i in 1:2
            new_state[i] += new_state[i+2]
        end
        # Calculate projected trajectory
        if (ylims[1] <= new_state[2] <= ylims[2]) &&
            (xlims[current_state[2]][1] <= new_state[1] <= xlims[current_state[2]][2]) &&
            (xlims[new_state[2]][1] <= current_state[1] <= xlims[new_state[2]][2]) &&
            (xlims[new_state[2]][1] <= new_state[1] <= xlims[new_state[2]][2])
            current_state = copy(new_state)
        else
            current_state = rand(start_states)
        end
        if n > 100000
            return "STOP"
        end
    end
    push!(state_action_array, [current_state,[0,0]])
    return state_action_array
end


### Plotting the Racetrack

rectangle(w, h, x, y) = Shape(x .+ [0,w,w,0], y .+ [0,0,h,h])
fig = plot(xlims = [0,32], ylims = [0,30], xticks = 0:2:32, 
        yticks = 0:2:30, aspect_ratio=:equal, 
        legend=:bottomright, palette =:Paired_12)

function plot_racetrack(race_track)
    lower_xlims = vcat([xlim[1] - 1 for xlim in race_track.xlims])
    upper_xlims = [xlim[2] for xlim in race_track.xlims]
    lower_xlims[length(lower_xlims)] = upper_xlims[length(upper_xlims)]
    plot!(lower_xlims, race_track.ylims[1]:race_track.ylims[2], color = "black", linetype = :steppre, label = "")
    plot!(upper_xlims, race_track.ylims[1]-1:race_track.ylims[2]-1, color = "black", linetype = :steppre, label = "")
    plot!(rectangle(10,1,0,0), color = "red", opacity=.5, label = "Start")
    plot!(rectangle(1,10,race_track.finish_states[1][1],race_track.finish_states[1][2] - 1), color = "green", opacity=.5, label = "Finish")
end

### Plotting the trajectories from every possible starting state

function plot_trajectories(race_track, policy)
    colors = distinguishable_colors(10)
    linestyles = [:solid, :dash, :dot, :dashdot, :dashdotdot, :solid, :dash, :dot, :dashdot, :dashdotdot,]
    linewidths = [x for x in 3:-0.2:1]
    for (state,col,linestyle,linewidth) in zip(start_states,colors,linestyles, linewidths)
        state_action_array = generate_episode(policy, 0, state, race_track.finish_states, race_track.ylims, race_track.velocity_limits)
        if state_action_array != "STOP"
            len = length(state_action_array)
            states_x = [state[1] for (state,action) in state_action_array]
            states_y = [state[2] for (state,action) in state_action_array]
            for i in 2:len-1
                plot!(fig, states_x[i-1:i], states_y[i-1:i], linetype=:steppre, linestyle = linestyle, linewidth = linewidth, arrow = true, color = col, label = "")
            end
            plot!(fig, states_x[len-1:len], states_y[len-1:len], linetype=:steppre, linestyle = linestyle, linewidth = linewidth, arrow = true, color = col, label = len)
        end
    end
end

# Code Execution

race_track = race_track1
epsilon = 0.4
alpha = 1/1000
max_iterations = 50000

Q, policy = monte_carlo(race_track, actions, epsilon, alpha, max_iterations)

plot_racetrack(race_track)

plot_trajectories(race_track, policy)

fig





# ### Animation Tests

# # anim = @animate for i = 1:length(states_x)
# #     plot(states_x[1:i], states_y[1:i], linetype=:steppre, legend=false)
# # end
 
# # gif(anim, "tutorial_anim_fps30.gif", fps = 30)

# # @gif for i = 1:length(states_x)
# #     plot!(states_x[1:i], states_y[1:i], linetype=:steppre, legend=false)
# # end


# ### Debugging


# # for y in 1:3
# #     for x in 1:10
# #         for vel_x in 0:2, vel_y in 0:2
# #             state = [x,y,vel_x,vel_y]
# #             println("State: ", state, "Counter: ", [counter[[state,action]] for action in actions])
# #         end
# #     end
# # end

# # for y in 1:5
# #     counter2 = 0
# #     total = 0
# #     for x in 1:10
# #         for x_vel in 0:2
# #             for y_vel in 0:2
# #                 for action in actions
# #                     if Q[[[x,y,x_vel,y_vel],action]] == 0
# #                         counter2 += 1
# #                     end
# #                     total += 1
# #                 end
# #             end
# #         end
# #     end
# #     println("Y:", y, "Zeros:", counter2, "Total:", total)
# # end
