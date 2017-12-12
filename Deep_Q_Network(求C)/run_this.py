#from maze_env import Maze
from RL_brain import DeepQNetwork
from matlab_env import matlab

def run_maze():
    step = 0
    bestminima=10
    for episode in range(500):
        # initial observation
        observation = env.reset()
        
        
        while True:
            # fresh env
        #    env.render()

            # RL choose action based on observation
            action = RL.choose_action(observation)

            # RL take action and get next observation and reward
            observation_, reward, done = env.step(action)

            RL.store_transition(observation, action, reward, observation_)

            if (step > 200) and (step % 5 == 0):
                RL.learn()

            # swap observation
            observation = observation_

            # break while loop when end of this episode
            if done:
                break
            step += 1
        if env.minima<bestminima:
            bestminima=env.minima
            bestx1=env.x1
            bestx2=env.x2
    # end of game
    print('\ngame over\n')
 #   env.destroy()
    print('best_minima:%f,best_x1:%f,best_x2:%f'%(bestminima,bestx1,bestx2))

if __name__ == "__main__":
    # maze game
    env = matlab()
    RL = DeepQNetwork(env.n_actions, env.n_features,
                      learning_rate=0.01,
                      reward_decay=0.9,
                      e_greedy=0.9,
                      replace_target_iter=200,
                      memory_size=2000,
                      output_graph=False,
                      double_q=False,
                      dueling=True
                      )
    run_maze()
#    env.after(100, run_maze)
#    env.mainloop()
    RL.plot_cost()