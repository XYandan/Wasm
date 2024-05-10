import matplotlib.pyplot as plt
import numpy as np

plt.rc('font', family='consolas')

null = 0

contracts = ['bit', 'contract', 'erc20', 'forwarder', 'gambling', 'global', 'hash', 'invoke', 'map', 'math', 'memory',
             'proxy', 'storage', 'transfer', 'wallet', 'null', 'null_f']
evm_codesize = {
    'g': [1050, 734, 2546, 2774, 2452, 1238, 676, 630, 496, 1168, 2184, 1854, 438, 534, 1726, 164, 308],
    'o': [790, 734, 2546, 2774, 2452, 1238, 676, 630, 496, 878, 1638, 1854, 438, 534, 1726, 164, 308],
    'p': [910, 734, 2546, 2774, 2452, 1238, 676, 630, 496, 1000, 1760, 1854, 438, 534, 1726, 164, 308]
}
wasm_codesize = {
    'g': [3806, null, 15696, null, null, 4045, 1743, null, 2981, 5744, 14743, null, 1861, 1452, null, 258, 524],
    'o': [14689, 10959, 23072, 18850, 22762, 12396, 12089, 8590, 13373, 15426, 13268, 13778, 11344, 8899, 16476, 6038,
          6671],
    'p': [6044, 7863, 21563, 16391, 15741, 7402, 5258, 6447, 11573, 6620, 5182, 16699, 5963, 4496, 12323, 3310, 3469]
}
category_colors = plt.get_cmap('Paired')(np.linspace(0.15, 0.85, 5))
plt.switch_backend('TkAgg')
fig, ax = plt.subplots(figsize=(16, 6))
width = 0.25  # the width of the bars

x = np.arange(len(contracts[:-2]))  # the label locations

clients = {'g': 'Geth', 'o': 'Openethereum', 'p': 'PlatON-Go'}

for i, (client_code, client_name) in enumerate(clients.items()):
    bars = ax.bar(x + i * width, [wasm_codesize[client_code][j] / evm_codesize[client_code][j] for j in x],
                  width, label=client_name, color=category_colors[i],bottom = 0)
    for bar in bars:
        height = bar.get_height()
        if height == 0:
            continue
        ax.text(bar.get_x() + bar.get_width() / 2., height,
                '%0.2f' % height, ha='center', va='bottom', fontsize=7)

ax.set_xlabel('合约名', {'family': 'SimSun', 'weight': 'normal', 'size': 25})
ax.set_ylabel('合约字节码长度比例', {'family': 'SimSun', 'weight': 'normal', 'size': 25})
ax.set_xticks(x + width)
ax.set_xticklabels(contracts[:-2], rotation=45, fontsize=20)
ax.legend()

legend = ax.legend(fontsize=16)

# plt.title('合约字节码长度比例')
plt.tight_layout()
plt.savefig('codesize_tot.pdf', dpi=600, bbox_inches='tight')
plt.show()
