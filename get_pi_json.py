from collections import deque
import json

def pi_digits():
    """生成圆周率小数点后的每一位数字"""
    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3
    while True:
        if 4 * q + r - t < n * t:
            yield n
            q, r, t, k, n, l = (
                10*q, 10*(r - n*t), t, k,
                (10*(3*q + r) // t) - 10*n, l)
        else:
            q, r, t, k, n, l = (
                q*k, (2*q + r)*l, t*l, k+1,
                (q*(7*k + 2) + r*l) // (t*l), l+2)

def find_sequence_in_pi(s):
    s=str(s)
    if not s.isdigit():
        print("错误：输入必须为纯数字。")
        return
    if len(s) == 0:
        print("错误：输入不能为空。")
        return
    
    target_len = len(s)
    window = deque(maxlen=target_len)
    pi_gen = pi_digits()
    position = 0
    
    try:
        while True:
            digit = next(pi_gen)
            position += 1
            window.append(str(digit))
            
            # 当窗口填满时开始检查
            if position >= target_len:
                current = ''.join(window)
                if current == s:
                    start_pos = position - target_len
                    print(f"找到匹配！您输入的序列出现在圆周率小数点后的第{start_pos}位。")
                    return start_pos
    except KeyboardInterrupt:
        print("\n搜索被中断。可能已超过当前计算限制。")

if __name__ == "__main__":
    z=[]
    for i in range(1,13):
            for j in range(1,32):
                s = i*100+j
                if s<1000:
                    s = '0'+str(s)
                else:
                    s = str(s)
                z.append({"数字":s,"位数":find_sequence_in_pi(s)})
                with open('pi.json', 'w', encoding='utf-8') as file:
                    json.dump(z, file, ensure_ascii=False, indent=2)
            print(z)
