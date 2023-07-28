import matplotlib.pyplot as plt
import numpy as np

# you might see an error that the module "tkinter" is not installed. If on Mac Os you can install it through the terminal via "brew install python-tk@3.9". General help can as always be found on stackoverflow: "https://stackoverflow.com/questions/25905540/importerror-no-module-named-tkinter" 

np.random.seed(10)

bandit_probabilities = [0.10, 0.40, 0.10, 0.10]


# environment
def step(action):
    rand = np.random.random()  # [0.0,1.0)
    reward = 1.0 if (rand < bandit_probabilities[action]) else 0.0
    return reward

def epsilon_greedy_policy(epsilon, actions, q_values):
    if np.random.binomial(1, epsilon) == 1:
        return np.random.choice(actions)
    else:
        return np.random.choice([action_ for action_, value_ in enumerate(q_values) if value_ == np.max(q_values)])

def upper_confidence_bound_policy(c, actions, q_values, iteration, num_invocations):
    upper_confidence_bounds = [q_values[action] + c * np.sqrt(np.log(iteration + 1) / (num_invocations[action])) if num_invocations[action] > 0 else np.inf for action in actions]
    return np.random.choice([action_ for action_, value_ in enumerate(upper_confidence_bounds) if value_ == np.max(upper_confidence_bounds)])

#Bonus: Not covered in class
def gradient_based_policy(actions, probabilities):
    return np.random.choice(actions, p=probabilities)

def compute_regret(q_star, arms, time_steps):
    probs = [bandit_probabilities[arm] for arm in arms]
    return np.cumsum(np.ones(time_steps)) * np.amax(q_star) - np.cumsum(probs)


def cumulative_average_mean(r, n):
    return np.cumsum(r) / np.cumsum(np.ones(n))


def plot_rewards(reward_list, n):
    for r in reward_list:
        plt.plot(cumulative_average_mean(r[0], n))
    plt.xlabel('Steps')
    plt.ylabel('Average reward')
    legend_str = [r[1] for r in reward_list]
    plt.legend(legend_str)
    plt.show()

def plot_regrets(regrets):
    for a in regrets:
        plt.plot(a[0])
    plt.xlabel('Steps')
    plt.ylim(0.0,50.0)
    plt.ylabel('Regret')
    legend_str = [r[1] for r in regrets]
    plt.legend(legend_str)
    plt.show()

def apply_epsilon_greedy(n_bandits, action_space, n_trials, timesteps, epsilons, arms):
    rewards = np.zeros((len(epsilons), n_trials, timesteps), dtype=np.float)
    regrets = np.zeros((len(epsilons), n_trials, timesteps), dtype=np.float)

    for eps_counter, eps in enumerate(epsilons):
        for trial in range(n_trials):
            n = np.zeros(n_bandits, dtype=np.int)
            q = np.zeros(n_bandits, dtype=np.float)
            for t in range(timesteps):
                action = epsilon_greedy_policy(eps, action_space, q)

                r = step(action)

                # updating action counter and Q
                n[action] += 1
                q[action] = q[action] + 1.0 / (n[action] + 1) * (r - q[action])
                # compute preference score
                # h[action] = q[action] + const * np.sqrt(np.log(t + 1) / n[action])

                rewards[eps_counter, trial, t] += r
                arms[t] = action

            regret = compute_regret(bandit_probabilities, arms, timesteps)
            regrets[eps_counter, trial, :] += regret

    rewards = np.mean(rewards, axis=1)
    regrets = np.mean(regrets, axis=1)

    rewards = list(rewards) 
    regrets = list(regrets)
    
    legend_entries = ["$\epsilon$-greedy $\epsilon=" + str(eps) + "$" for eps in epsilons] 

    rewards = list(zip(rewards, legend_entries))
    regrets = list(zip(regrets, legend_entries))


    return rewards,regrets

def apply_upper_confidence_bound_policy(n_bandits, action_space, n_trials, timesteps, arms, ucb_constants):
    # For different upper confidence bounds constants
    rewards = np.zeros((len(ucb_constants), n_trials, timesteps), dtype=np.float)
    regrets = np.zeros((len(ucb_constants), n_trials, timesteps), dtype=np.float)

    for ucb_constant_counter, ucb_constant in enumerate(ucb_constants):
        for trial in range(n_trials):
            n = np.zeros(n_bandits, dtype=np.int)
            q = np.zeros(n_bandits, dtype=np.float)
            preference_scores = np.zeros(n_bandits, dtype=np.float)

            for t in range(timesteps):
                
                action = upper_confidence_bound_policy(ucb_constant, action_space, q, t, n)

                r = step(action)

                # updating action counter and expected reward Q
                n[action] += 1
                q[action] = q[action] + 1.0 / (n[action] + 1) * (r - q[action])
                
                rewards[ucb_constant_counter, trial, t] += r
                arms[t] = action

            regret = compute_regret(bandit_probabilities, arms, timesteps)
            regrets[ucb_constant_counter, trial, :] += regret

    rewards = np.mean(rewards, axis=1)
    regrets = np.mean(regrets, axis=1)

    rewards = list(rewards) 
    regrets = list(regrets)
    
    legend_entries = ["UCB $c=" + str(ucb_constant) + "$" for ucb_constant in ucb_constants] 

    rewards = list(zip(rewards, legend_entries))
    regrets = list(zip(regrets, legend_entries))

    return rewards,regrets

# Bonus: Not covered in class
def apply_gradient_based_method(n_bandits, action_space, n_trials, timesteps,  arms, eta_parameters):
    rewards = np.zeros((len(eta_parameters), n_trials, timesteps), dtype=np.float)
    regrets = np.zeros((len(eta_parameters), n_trials, timesteps), dtype=np.float)

    for eta_parameter_counter, eta_parameter in enumerate(eta_parameters):
        for trial in range(n_trials):
            n = np.zeros(n_bandits, dtype=np.int)
            q = np.zeros(n_bandits, dtype=np.float)
            preference_scores = np.zeros(n_bandits, dtype=np.float)
            trial_rewards = rewards[eta_parameter_counter, trial, :]

            for t in range(timesteps):
                probabilities = np.asarray([np.exp(preference_score) for preference_score in preference_scores])
                probabilities /= np.sum(probabilities)
                action = gradient_based_policy(action_space, probabilities)

                r = step(action)

                # updating action counter and expected reward Q
                n[action] += 1
                q[action] = q[action] + 1.0 / (n[action] + 1) * (r - q[action])
                
                average_trial_reward = np.sum(trial_rewards)/(t+1)
                action_indicator = np.zeros(n_bandits, dtype=np.float)
                action_indicator[action] = 1.0
                preference_scores += eta_parameter * (r - average_trial_reward) * (action_indicator - probabilities[action])

                trial_rewards[t] += r
                arms[t] = action

            regret = compute_regret(bandit_probabilities, arms, timesteps)
            regrets[eta_parameter_counter, trial, :] += regret

    rewards = np.mean(rewards, axis=1)
    regrets = np.mean(regrets, axis=1)
    
    rewards = list(rewards) 
    regrets = list(regrets)
    
    legend_entries = ["gradient $\eta=" + str(eta_parameter) + "$" for eta_parameter in eta_parameters] 

    rewards = list(zip(rewards, legend_entries))
    regrets = list(zip(regrets, legend_entries))

    return rewards,regrets

def apply_thompson_sampling_policy(n_bandits, action_space, n_trials, timesteps, arms, alpha_beta_priors):
    # For different upper confidence bounds constants
    rewards = np.zeros((len(alpha_beta_priors), n_trials, timesteps), dtype=np.float)
    regrets = np.zeros((len(alpha_beta_priors), n_trials, timesteps), dtype=np.float)

    for prior_counter, alpha_beta_prior in enumerate(alpha_beta_priors):
        for trial in range(n_trials):
            alpha = alpha_beta_prior[0]
            beta  = alpha_beta_prior[1]
            successes = np.zeros(n_bandits, np.int)
            failures = np.zeros(n_bandits, np.int)
            theta = np.zeros(n_bandits, np.float)
            n = np.zeros(n_bandits, dtype=np.int)
            q = np.zeros(n_bandits, dtype=np.float)

            for t in range(timesteps):

                for bandit in range(n_bandits):
                    theta[bandit] = np.random.beta(successes[bandit] + alpha, failures[bandit] + beta)

                action = np.random.choice([action_ for action_, value_ in enumerate(theta) if value_ == np.max(theta)])

                r = step(action)

                # updating action counter and expected reward Q
                n[action] += 1

                successes[action] += (r == 1)
                failures[action] += (r == 0) 

                rewards[prior_counter, trial, t] += r
                arms[t] = action

            regret = compute_regret(bandit_probabilities, arms, timesteps)
            regrets[prior_counter, trial, :] += regret

    rewards = np.mean(rewards, axis=1)
    regrets = np.mean(regrets, axis=1)

    rewards = list(rewards) 
    regrets = list(regrets)
    
    legend_entries = ["Thompson $\\alpha=" + str(alpha_beta[0]) + ", \\beta=" + str(alpha_beta[1]) + "$" for alpha_beta in alpha_beta_priors] 

    rewards = list(zip(rewards, legend_entries))
    regrets = list(zip(regrets, legend_entries))

    return rewards,regrets

def main():
    number_of_bandits = len(bandit_probabilities) # = n_actions
    
    action_space = np.arange(number_of_bandits)

    #Parameters
    number_of_trials = 20 
    timesteps = 1000
    epsilons = [0.0, 0.01, 0.1]
    ucb_constants = [0.1,1.0,10.0]
    gradient_method_constants = [0.1, 1.0, 10]
    alpha_beta_priors = [[1.0,1.0], [1.0, 2.0]]

    arms = np.zeros(timesteps, dtype=np.int)

    rewards_epsilon_greedy, regrets_epsilon_greedy = apply_epsilon_greedy(number_of_bandits, action_space, number_of_trials, timesteps, epsilons, arms)

    rewards_ucb, regrets_ucb = apply_upper_confidence_bound_policy(number_of_bandits, action_space, number_of_trials, timesteps, arms, ucb_constants)

    rewards_gradient, regrets_gradient = apply_gradient_based_method(number_of_bandits, action_space, number_of_trials, timesteps, arms, gradient_method_constants)

    rewards_thompson, regrets_thompson = apply_thompson_sampling_policy(number_of_bandits, action_space, number_of_trials, timesteps, arms, alpha_beta_priors)

    reward_list = rewards_epsilon_greedy + rewards_ucb + rewards_gradient + rewards_thompson
    plot_rewards(reward_list, timesteps)

    regret_list = regrets_epsilon_greedy + regrets_ucb + regrets_gradient + regrets_thompson
    plot_regrets(regret_list)

if __name__ == '__main__':
    main()
