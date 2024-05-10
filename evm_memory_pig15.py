import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker


plt.rc('font', family='consolas')

null = 0

contracts = ['bit','contract','erc20','forwarder','gambling','global','hash','invoke','map','math','memory','proxy','storage','transfer','wallet','null_f']
evm_memory = {
    'g': [24268,45596,29677,34634,29194,28557,21435,30167,22753,25627,52620,36627,28397,28293,34186,31166],
    'o': [44016,46577,46765,46954,58969,44311,44016,45644,45666,44016,55920,45749,44366,45862,46683,43824],
    'p': [10480,29135,14343,18751,28799,15860,11951,20541,12109,10377,49895,26719,10989,14469,25285,9847],
    'e': [22976,34051,35878,36570,30600,23008,26672,26668,29061,22917,36865,34367,22602,39608,28867,22351]
}


category_colors = plt.get_cmap('Paired')(np.linspace(0.15, 0.85, 5))
plt.switch_backend('TkAgg')
fig, ax = plt.subplots(figsize=(16, 6))
width = 0.25 # the width of the bars

# x = np.arange(len(contracts[:-1]))  # the label locations
# print(x)
group_width = 0.25# the width of each group

x = np.arange(len(contracts[:-1])) * (len(evm_memory) * width + group_width)

clients = {'g': 'GethEVM', 'o': 'OpenEVM', 'p': 'PlatEVM','e':"evmone"}



print(x)
for i, (client_code, client_name) in enumerate(clients.items()):
    bars = ax.bar(x + i * width, [evm_memory[client_code][j] for j in np.arange(len(contracts[:-1]))],
                  width, label=client_name, color=category_colors[i],bottom = 0)
    for bar in bars:
        height = bar.get_height()
        if height == 0:
            continue
        ax.text(bar.get_x() + bar.get_width() / 2., height,
                '%0.2f' % (height / 10**4), ha='center', va='bottom', fontsize=8,rotation=60)

def format_y_ticks(value, pos):
    return '%0.2f' % (value / 10**4)

ax.yaxis.set_major_formatter(ticker.FuncFormatter(format_y_ticks))
ax.text(-0.5, 60000, '×$10^4$', ha='center', va='bottom', fontsize=15)

# ax.set_xlabel('合约名', {'family': 'SimSun', 'weight': 'normal', 'size': 20})
ax.set_ylabel('Memory Occupancy (byte)', {'family': 'consolas', 'weight': 'normal', 'size': 20})
ax.set_xticks(x  +  (len(evm_memory) - 1) * width / 2.)
ax.set_xticklabels(contracts[:-1], rotation=45, fontsize=20)
ax.legend()


# ax.spines['left'].set_position(('data', -0.5))
# ax.spines['left'].set_position('zero')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
# legend = ax.legend(fontsize=16)
legend = ax.legend(loc='upper right',bbox_to_anchor = (0.95,1.15) ,fontsize=12)
# plt.title('合约字节码长度比例')
plt.tight_layout()
plt.savefig('exec_mem_15.pdf', dpi=600, bbox_inches='tight')
plt.show()
