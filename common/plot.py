#!/usr/bin/env python
# coding=utf-8
'''
Author: John
Email: johnjim0816@gmail.com
Date: 2020-10-07 20:57:11
LastEditor: John
LastEditTime: 2021-09-23 12:23:01
Discription: 
Environment: 
'''
import matplotlib.pyplot as plt
import seaborn as sns
# from matplotlib.font_manager import FontProperties # 导入字体模块

# def chinese_font():  
#     ''' 设置中文字体
#     '''
#     return FontProperties(fname='/System/Library/Fonts/STHeiti Light.ttc',size=15)  # fname系统字体路径，此处是mac的
# def plot_rewards_cn(rewards,ma_rewards,tag="train",env='CartPole-v0',algo = "DQN",save=True,path='./'):
#     ''' 中文画图
#     '''
#     sns.set()
#     plt.figure()
#     plt.title(u"{}环境下{}算法的学习曲线".format(env,algo),fontproperties=chinese_font())
#     plt.xlabel(u'回合数',fontproperties=chinese_font())
#     plt.plot(rewards)
#     plt.plot(ma_rewards)
#     plt.legend((u'奖励',u'滑动平均奖励',),loc="best",prop=chinese_font())
#     if save:
#         plt.savefig(path+f"{tag}_rewards_curve_cn")
#     # plt.show()

def plot_rewards(rewards,ma_rewards,plot_cfg,tag='train'):
    sns.set() 
    plt.figure() # 创建一个图形实例，方便同时多画几个图
    plt.title("learning curve on {} of {} for {}".format(plot_cfg.device, plot_cfg.algo, plot_cfg.env))
    plt.xlabel('epsiodes')
    plt.plot(rewards,label='rewards')
    plt.plot(ma_rewards,label='ma rewards')
    plt.legend()
    if plot_cfg.save:
        plt.savefig(plot_cfg.result_path+"{}_rewards_curve".format(tag))
    plt.show()
# def plot_rewards(rewards,ma_rewards,tag="train",env='CartPole-v0',algo = "DQN",save=True,path='./'):
#     sns.set() 
#     plt.figure() # 创建一个图形实例，方便同时多画几个图
#     plt.title("average learning curve of {} for {}".format(algo,env))
#     plt.xlabel('epsiodes')
#     plt.plot(rewards,label='rewards')
#     plt.plot(ma_rewards,label='ma rewards')
#     plt.legend()
#     if save:
#         plt.savefig(path+"{}_rewards_curve".format(tag))
#     plt.show()

def plot_losses(losses,algo = "DQN",save=True,path='./'):
    sns.set()
    plt.figure()
    plt.title("loss curve of {}".format(algo))
    plt.xlabel('epsiodes')
    plt.plot(losses,label='rewards')
    plt.legend()
    if save:
        plt.savefig(path+"losses_curve")
    plt.show()
   
