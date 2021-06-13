using StatsBase



# Short corridor with switched actions

struct environment
    states
    start_states
    terminal_states
    actions
    gamma
end

states = collect(1:3)
start_states = collect(1:1)
terminal_states = collect(3:1)
actions = [-1, 1]
gamma = 1

corridor = environment(states, start_states, terminal_states, actions, gamma)

function transition(state, action)
    if state == 1
        return state - action, -1, false
    elseif state + action == 3
        return state + action, -1, true
    else
        return max(0, state + action), -1, false
    end
end


function features(state, action)
    if action == 1
        return [1,0]
    else
        return [0,1]
    end
end

function policy(state, theta, environment)
    p_array = [exp(vecdot(theta, features(state,action))) for action in environment.actions]
    return p_array/sum(p_array)
end

function choose_action(state, theta, environment)
    weights = policy(state, theta, environment)
    return sample(action, Weights(weights))[0]
end


function REINFORCE(environment, max_episodes)
    theta = zeros(2)
    episode_length_array = fill(10,max_episodes)

    for i in 1:max_episodes
        done = false
        state = rand(environment.start_states)
        S = [state]
        A = []
        R = [0]

        
        T = 0
        while !done
            action = choose_action(state, theta, environment)
            state, reward, done = transition(state, action)
            
            S.append(state)
            A.append(action)
            R.append(reward)

            T += 1
            if done
                episode_length_array[i] = T
                if i%20 == 0
                    print("Episode $i finished after $T timesteps")
                    
                    if T < 100
                        mean = np.mean(episode_length_array[1:T])
                    else
                        mean = np.mean(episode_length_array[T-99:T])
                    end
                    print("Average length (last 100): ", mean)
                break
                end
            end
        end

        for t in range(T)
            G = sum([gamma^(k-t-1)*R[k] for k in range(t+1,T+1)])
            probabilities = policy(S[t], theta, env)
            features = [x(S[t],action) for action in actions]
            gradient = x(S[t],A[t]) - vecdot(probabilities, features)
            theta += alpha*gamma^t*(G-10)*gradient
        end
        #print("Theta: ", theta)
    end
    print(episode_length_array)
    return theta
    
end

theta = REINFORCE(corridor, 100)

print(theta)