import gymnasium as gym
from gymnasium import Wrapper
from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.monitor import Monitor

def custom_reward(observation, reward, done):
    x_position = observation[0]  # 小车的位置
    theta = observation[2]  # 杆的角度
    
    # 对位置和角度都进行惩罚
    position_penalty = -(x_position ** 2) * 0.2
    angle_penalty = -(theta ** 2) * 1.0  # 根据实际需要调整系数
    
    return reward + position_penalty + angle_penalty, done

class CustomRewardWrapper(Wrapper):
    def step(self, action):
        observation, reward, terminated, truncated, info = self.env.step(action)
        reward, _ = custom_reward(observation, reward, terminated or truncated)
        return observation, reward, terminated, truncated, info

# -------------------------- 训练阶段（不渲染） --------------------------
# 创建训练环境（关闭渲染）
train_env = gym.make("CartPole-v1")
# train_env = CustomRewardWrapper(train_env)  # 自定义奖励
train_env = Monitor(train_env)  # 监控训练数据

# 初始化PPO模型
model = PPO(
    "MlpPolicy",
    train_env,
    verbose=1,           # 显示训练日志
    device="cpu",        # 使用CPU训练
    tensorboard_log="./logs/"  # TensorBoard日志路径
)

# 训练模型（10000步，约10秒内完成）
model.learn(total_timesteps=10_000)

# 关闭训练环境
train_env.close()

# -------------------------- 测试阶段（渲染画面） --------------------------
# 创建测试环境（启用渲染）
test_env = gym.make("CartPole-v1", render_mode="human")

# 测试训练后的策略
obs, _ = test_env.reset()
sum_reward = 0
for _ in range(1000):
    action, _ = model.predict(obs, deterministic=True)
    obs, reward, done, _, _ = test_env.step(action)
    sum_reward += reward
    if done:
        obs, _ = test_env.reset()  # 重置环境
        print(f"Reward: {sum_reward:.2f}")
        sum_reward = 0

# 关闭测试环境
test_env.close()