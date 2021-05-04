using BenchmarkTools


function policy_evaluation(policy, S, R, tau)

    V = fill(0.0,length(S))
    counter = 0

    while true
        delta = 0
        for s in S
            v = V[s]
            if 1 < s && s < 10
                V[s] = policy[s]*(V[s-1] + R[s-1]) + (1 - policy[s])*(V[s+1] + R[s+1])
            end
            delta = max(delta, abs(v - V[s]))
        end
        counter += 1
        if delta < tau
            return V, counter
        end
    end

end

function policy_improvement(policy, S, R, V)
    policy_stable = true
    for s in S
        old_policy = policy[s]
        if 1 < s < 10
            if V[s+1] + R[s+1] > V[s-1] + R[s-1]
                policy[s] = 0
            else
                policy[s] = 1
            end
            if old_policy != policy[s]
                policy_stable = false
            end
        end
    end
    return policy, policy_stable
end

function policy_iteration(tau)
    policy = fill(1/2, 10)
    S = [x for x in 1:10]
    R = vcat(10, fill(0,8), -5)
    V, iteration_counter = policy_evaluation(policy, S, R, tau)
    policy, policy_stable = policy_improvement(policy, S, R, V)
    random_evaluation = V
    random_num_iterations = iteration_counter
    counter = 0
    while policy_stable == false
        V,_ = policy_evaluation(policy, S, R, tau)
        policy, policy_stable = policy_improvement(policy, S, R, V)
        counter += 1
    end
    return policy, V, counter, random_evaluation, random_num_iterations
end

#tolerance
tau = 10e-6


bench = @benchmark policy_iteration(tau)

io = IOBuffer()

show(io, "text/plain", bench)

s = String(take!(io))

println(s)

policy, V, counter, random_evaluation, random_num_iterations = policy_iteration(tau)

println("Evaluation of random policy:", round.(random_evaluation, digits = 2))

println("Number of iterations:", random_num_iterations)

println("V:", V)

println("policy:", policy)

println("Number of policy improvements:", counter)