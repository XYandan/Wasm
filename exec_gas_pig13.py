import matplotlib.pyplot as plt
import numpy as np

plt.rc('font', family='consolas')

null = 0

contracts = ['bit','contract','erc20','forwarder','gambling','global','hash','invoke','map','math','memory','proxy','storage','transfer','wallet','null','null_f']
evm_exec_gas = {
    'g': [21967,54470,31890,29325,94824,21548,22447,24523,31980,22078,49799,36245,24222,30962,35431,21377],
    'o': [21967,54470,31890,29325,94824,21548,22447,24523,31980,22078,49799,36245,24222,30962,35431,21377],
    'p': [21967,54470,31890,29325,94824,21548,22447,24523,31980,22078,49799,36245,24222,30962,35431,21377]
}
wasm_exec_gas = {
    'g': [22985,null,36584,null,null,22282,23792,null,34425,23704,91816,null,24918,null,null,21344],
    'o': [31030,80148,46007,38390,104220,29907,38155,31388,47885,31464,57348,60643,32182,32069,42612,28319],
    'p': [30020,null,2407286,69641,523130,28823,32072,38605,726796,31794,39254,null,32726,42270,90774,25283]
}

category_colors = plt.get_cmap('Paired')(np.linspace(0.15, 0.85, 5))
plt.switch_backend('TkAgg')
fig, ax = plt.subplots(figsize=(16, 6))
width = 0.25  # the width of the bars

x = np.arange(len(contracts[:-2]))  # the label locations

clients = {'g': 'Geth', 'o': 'Openethereum', 'p': 'PlatON-Go'}

for i, (client_code, client_name) in enumerate(clients.items()):
    bars = ax.bar(x + i * width, [np.log2(wasm_exec_gas[client_code][j] / evm_exec_gas[client_code][j]) for j in x],
                  width, label=client_name, color=category_colors[i],bottom = 0)
    for bar in bars:
        height = bar.get_height()
        if height == 0:
            continue
        elif height > 0:
            ax.text(bar.get_x() + bar.get_width() / 2., height,
                    '%0.2f' % height, ha='center', va='bottom', fontsize=7)
        else:
            ax.text(bar.get_x() + bar.get_width() / 2., height - 0.2,
                    '%0.2f' % height, ha='center', va='bottom', fontsize=7)

ax.spines['bottom'].set_position('zero')

# plt.xlabel('合约名',labelpad=-12,fontsize = 25)
# ax.set_xlabel('合约名', {'family': 'SimSun', 'weight': 'normal', 'size': 20})
ax.set_ylabel('Gas(Wasm)/Gas(EVM)', {'family': 'consolas', 'weight': 'normal', 'size': 20})
# ax.set_yscale('log') # Y轴，10为底，科学计数
ax.text(-0.5, 6.25, '$log_{2}$', ha='center', va='bottom', fontsize=15,fontstyle='normal')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
# ax.set_xticks(x + width)
# ax.set_xticklabels(contracts[:-2], rotation=45, fontsize=20, verticalalignment='top')
# ax.xticks(contracts[:-2], rotation=45, fontsize=20, ha='right',position = (0,-1))
plt.xticks(x + width, contracts[:-2], rotation=45, fontsize=20, position = (0,-0.5))
ax.legend()

legend = ax.legend(fontsize=16)
# ax.set_ylim(bottom=0)

# ax.set_ylim(bottom=-0.5)
#
# # Set the x-axis position to be in the middle of the y-axis

#
# # Draw the vertical line for the y-axis
# ax.axhline(0, color='black', linewidth=0.5)
# ax.axhline(y=0, color='black', linewidth=0.8)
# plt.title('合约字节码长度比例')
plt.tight_layout()
plt.savefig('exec_gas_pig13.pdf', dpi=600, bbox_inches='tight')
plt.show()
