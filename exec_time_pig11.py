import matplotlib.pyplot as plt
import numpy as np

plt.rc('font', family='consolas')

null = 0

contracts = ['bit','contract','erc20','forwarder','gambling','global','hash','invoke','map','math','memory','proxy','storage','transfer','wallet','null_f']
evm_exec_time = {
    'g': [265708,329076,298299,331514,280340,301768,239799,242481,235716,287694,423722,299261,306337,263031,268703,322940],
    'o': [73887,70348,92568,94106,155899,70416,79755,80390,83177,74672,681205,112481,73738,77750,88660,65035],
    'p': [571657,735962,701812,716212,756502,518891,699053,619426,653179,576302,837002,664522,527191,595991,677565,511678]
}
wasm_exec_time = {
    'g': [1104737,null,2225797,null,null,1116024,897467,null,1112495,1303512,7573780,null,861886,null,null,604543],
    'o': [1189215,1122263,1808778,1540053,1810406,988173,1195657,634723,1215846,1228364,2116959,1590676,779810,1766240,1317152,540256],
    'p': [803146,null,25836375,1117445,5310521,23128022,924548,1094661,8245807,885789,874753,null,882342,885188,1531681,806790]
}



category_colors = plt.get_cmap('Paired')(np.linspace(0.15, 0.85, 5))
plt.switch_backend('TkAgg')
fig, ax = plt.subplots(figsize=(16, 6))
width = 0.25  # the width of the bars

x = np.arange(len(contracts[:-2]))  # the label locations

clients = {'g': 'Geth', 'o': 'Openethereum', 'p': 'PlatON-Go'}

for i, (client_code, client_name) in enumerate(clients.items()):
    bars = ax.bar(x + i * width, [wasm_exec_time[client_code][j] / evm_exec_time[client_code][j] for j in x],
                  width, label=client_name, color=category_colors[i],bottom = 0)
    for bar in bars:
        height = bar.get_height()
        if height == 0:
            continue
        ax.text(bar.get_x() + bar.get_width() / 2., height,
                '%0.2f' % height, ha='center', va='bottom', fontsize=7)

# ax.set_xlabel('合约名', {'family': 'SimSun', 'weight': 'normal', 'size': 25})
ax.set_ylabel('Time(Wasm)/Time(EVM)', {'family': 'consolas', 'weight': 'normal', 'size': 25})
ax.set_xticks(x + width)
ax.set_xticklabels(contracts[:-2], rotation=45, fontsize=20)
ax.legend()


ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

legend = ax.legend(fontsize=16)

# plt.title('合约字节码长度比例')
plt.tight_layout()
plt.savefig('exec_time_11.pdf', dpi=600, bbox_inches='tight')
plt.show()
