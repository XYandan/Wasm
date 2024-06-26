import matplotlib.pyplot as plt
import numpy as np

plt.rc('font', family='consolas')

null = 0

contracts = ['bit','contract','erc20','forwarder','gambling','global','hash','invoke','map','math','memory','proxy','storage','transfer','wallet','null_f']
evm_memory = {
    'g': [24268,45596,29677,34634,29194,28557,21435,30167,22753,25627,52620,36627,28397,28293,34186,31166],
    'o': [44016,46577,46765,46954,58969,44311,44016,45644,45666,44016,55920,45749,44366,45862,46683,43824],
    'p': [10480,29135,14343,18751,28799,15860,11951,20541,12109,10377,49895,26719,10989,14469,25285,9847]
}
wasm_memory = {
    'g': [96042,null,218624,null,null,98358,78643,null,99447,118053,831000,null,71902,null,null,48400],
    'o': [2416456,2098140,2948449,2841067,2697571,2274412,2231768,1871356,2286608,2422272,2473520,2492911,1994218,1888176,2507985,1706248],
    'p': [167583,null,2560500,261550,664120,8217406,169095,333137,894606,169107,163889,null,172567,171933,334956,162025]
}

category_colors = plt.get_cmap('Paired')(np.linspace(0.15, 0.85, 5))
plt.switch_backend('TkAgg')
fig, ax = plt.subplots(figsize=(16, 6))
width = 0.25  # the width of the bars

x = np.arange(len(contracts[:-2]))  # the label locations

clients = {'g': 'Geth', 'o': 'Openethereum', 'p': 'PlatON-Go'}

for i, (client_code, client_name) in enumerate(clients.items()):
    bars = ax.bar(x + i * width, [(wasm_memory[client_code][j] / evm_memory[client_code][j] if wasm_memory[client_code][j] / evm_memory[client_code][j] > 1. else 1.05) for j in x],
                  width, label=client_name, color=category_colors[i],bottom = 0)
    # for bar in bars:
    #     height = bar.get_height()
    #     if height == 0:
    #         continue
    #     ax.text(bar.get_x() + bar.get_width() / 2., height,
    #             '%0.2f' % height, ha='center', va='bottom', fontsize=7)

# ax.set_xlabel('合约名', {'family': 'SimSun', 'weight': 'normal', 'size': 20})
ax.set_ylabel('Mem(Wasm)/Mem(EVM)', {'family': 'consolas', 'weight': 'normal', 'size': 15})
ax.set_xticks(x + width)
ax.set_xticklabels(contracts[:-2], rotation=30, fontsize=15,position = (0,0.01))
ax.legend()

ax.set_yscale('log') # Y轴，10为底，科学计数
# ax.set_ylim(1,10**3)
plt.yticks([1, 10, 100, 1000], ['$10^0$', '$10^1$', '$10^2$',  '$10^3$'])

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
legend = ax.legend(loc='upper right',bbox_to_anchor = (0.85,0.9),fontsize=11)

# plt.title('合约字节码长度比例')
plt.tight_layout()
plt.savefig('./fig/memory.pdf', dpi=600, bbox_inches='tight')
plt.show()
