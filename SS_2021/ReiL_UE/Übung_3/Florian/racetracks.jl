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
