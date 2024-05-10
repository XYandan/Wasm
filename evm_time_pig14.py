import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker


plt.rc('font', family='consolas')

null = 0

contracts = ['bit','contract','erc20','forwarder','gambling','global','hash','invoke','map','math','memory','proxy','storage','transfer','wallet','null_f']
evm_exec_time = {
    'g': [265708,329076,298299,331514,280340,301768,239799,242481,235716,287694,423722,299261,306337,263031,268703,322940],
    'o': [73887,70348,92568,94106,155899,70416,79755,80390,83177,74672,681205,112481,73738,77750,88660,65035],
    'p': [571657,735962,701812,716212,756502,518891,699053,619426,653179,576302,837002,664522,527191,595991,677565,511678],
    'e': [272465,356785,396874,416352,354098,262778,302181,321312,318225,263700,308313,409013,251457,432704,310314,267182]
}

category_colors = plt.get_cmap('Paired')(np.linspace(0.15, 0.85, 5))
plt.switch_backend('TkAgg')
fig, ax = plt.subplots(figsize=(16, 6))
width = 0.25 # the width of the bars

# x = np.arange(len(contracts[:-1]))  # the label locations
# print(x)
group_width = 0.25# the width of each group

x = np.arange(len(contracts[:-1])) * (len(evm_exec_time) * width + group_width)

clients = {'g': 'GethEVM', 'o': 'OpenEVM', 'p': 'PlatEVM','e':"evmone"}



print(x)
for i, (client_code, client_name) in enumerate(clients.items()):
    bars = ax.bar(x + i * width, [evm_exec_time[client_code][j] for j in np.arange(len(contracts[:-1]))],
                  width, label=client_name, color=category_colors[i],bottom = 0)
    for bar in bars:
        height = bar.get_height()
        if height == 0:
            continue
        ax.text(bar.get_x() + bar.get_width() / 2., height,
                '%0.2f' % (height / 10**6), ha='center', va='bottom', fontsize=9,rotation=60)

def format_y_ticks(value, pos):
    return '%0.2f' % (value / 10**6)

ax.yaxis.set_major_formatter(ticker.FuncFormatter(format_y_ticks))
# ax.text(-0.5, 850000, '×$10^5$', ha='center', va='bottom', fontsize=15)

ax.set_xlabel('', {'family': 'SimSun', 'weight': 'normal', 'size': 25})
ax.set_ylabel('Time Consumption', {'family': 'SimSun', 'weight': 'normal', 'size': 25})
ax.set_xticks(x  +  (len(evm_exec_time) - 1) * width / 2)
ax.set_xticklabels(contracts[:-1], rotation=45, fontsize=20)
ax.legend()

# ax.spines['left'].set_position('zero')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
# legend = ax.legend(fontsize=16)
legend = ax.legend(loc='upper left', fontsize=12)
# plt.title('合约字节码长度比例')
plt.tight_layout()
plt.savefig('exec_time_14.pdf', dpi=600, bbox_inches='tight')
plt.show()
