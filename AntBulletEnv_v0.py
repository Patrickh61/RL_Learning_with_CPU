import gymnasium as gym
from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.vec_env import DummyVecEnv

# -------------------------- 训练阶段（不渲染） --------------------------
# 创建训练环境（MuJoCo Ant-v4）
# def create_train_env():
#     env = gym.make("Ant-v4", render_mode="none")  # 关闭GUI渲染
#     return env

# # 包装为向量环境（单环境）
# train_env = DummyVecEnv([create_train_env])

# # 初始化PPO模型（CPU训练配置）
# model = PPO(
#     "MlpPolicy",
#     train_env,
#     verbose=1,                # 显示训练日志
#     device="cpu",             # 强制使用CPU
#     tensorboard_log="./logs", # TensorBoard日志路径
#     batch_size=64,            # 减小批量大小适配CPU内存
#     n_steps=2048,             # 每轮收集的步数
#     learning_rate=3e-4,       # 学习率
#     policy_kwargs={"net_arch": [256, 256]}  # 更深的网络
# )

# # 训练模型（500,000步，约1-2小时，取决于CPU性能）
# model.learn(total_timesteps=500_000)

# # 保存模型
# model.save("ppo_ant_mujoco_cpu")

# # 关闭训练环境
# train_env.close()
# print("AntBulletEnv Training completed.")
# -------------------------- 测试阶段（渲染画面） --------------------------
# 创建测试环境（启用渲染）
test_env = gym.make("Ant-v4", render_mode="human")

# 加载训练好的模型
model = PPO.load("ppo_ant_mujoco_cpu", env=test_env)

# 运行测试循环
obs, _ = test_env.reset()
for _ in range(3000):
    action, _ = model.predict(obs, deterministic=True)
    obs, reward, done, truncated, info = test_env.step(action)
    
    if done or truncated:
        obs, _ = test_env.reset()  # 环境终止或截断时重置

test_env.close()