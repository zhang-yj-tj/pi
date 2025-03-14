# 在π中找到您的专属序列 / Pi Digit Explorer - Find Your Special Sequence in π

## 项目概述 / Project Overview
本项目提供完整的解决方案，用于在圆周率π的小数点后定位任意数字序列的首现位置，并通过自动化流程实现数据生成、处理与可视化展示。系统采用模块化设计，包含π数字生成、实时序列匹配、数据持久化、智能排序和交互式展示等功能模块。

This project provides a complete solution for locating the first occurrence position of any digit sequence in the decimal expansion of π (pi), with automated workflow covering data generation, processing and visualization. The system features modular design including π digit generation, real-time sequence matching, data persistence, intelligent sorting and interactive display.

## 功能模块 / Functional Modules

### 1. π数字生成引擎 / Pi Digit Generation Engine (`pi_digits` 函数)
- 基于Spigot算法的高效生成器实现，支持无限位数的π数字流式输出 / Implements Spigot algorithm based generator for streaming output of π digits
- 单精度浮点运算优化，运算速度较快 / Single-precision floating-point operation optimization, faster operation speed

### 2. 实时序列匹配器 / Real-time Sequence Matcher (`find_sequence_in_pi` 函数)
- 滑动窗口算法结合双端队列(deque)实现高效匹配 / Sliding window algorithm with deque implementation for efficient matching 

### 3. 数据持久化模块 / Data Persistence Module (`get_pi_json.py`)
- 生成结构化JSON数据，包含： / Generates structured JSON data including:
  - 数字序列 / digit sequence
  - 首现位置 / First occurrence position
  - 位置排名百分比 / Position Rank Percentage

### 4. 数据分析器 / Data Analyzer (`judge_json.py`)
- 生成结构化JSON数据，包含： / Generates structured JSON data including:
  - 数字序列 / digit sequence
  - 首现位置 / First occurrence position
  - 位置排名百分比 / Position Rank Percentage

### 5. 交互式展示系统 / Interactive Display System (`main.html`)
- 响应式网页设计，支持移动端/桌面端 / Responsive web design for mobile/desktop
- 可视化结果展示，交互式位置导航 / Visual result display, interactive location navigation
- π节特别主题 / Pi section special theme

## 使用方法 / Usage
- 下载`main.html`在浏览器中打开即可 / Download `main.html` and open it in your browser.
- 输入4位生日数字（输入其他数字将实时计算） / Enter 4 birthday numbers (entering other numbers will be calculated in real time)



# 在无限不循环中找到你的专属位置吧！ / Find your place in the infinite loop!


📬 联系作者 / Contact
电子邮箱 / Email: zhang.ershi@qq.com
微信号 / WeChat: zhang_tjnk
