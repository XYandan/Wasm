import matplotlib.pyplot as plt
import numpy as np

plt.rc('font', family='consolas')

null = 0

contracts = ['bit','contract','erc20','forwarder','gambling','global','hash','invoke','map','math','memory','proxy','storage','transfer','wallet','null_f']
evm_io = {
    'g': [16785218,8529725,27048880,13321412,4103273,23728722,5045125,3773508,7852451,16806026,11702445,10335022,6544687,4618604,13915107,3061195],
    'o': [87112867,956310,273062676,114682469,52042011,276406923,24578547,25424827,65178601,87120165,85276391,28827866,57090855,38709018,152481482,23561135],
    'p': [72691578,57298019,157000268,67660966,29317861,154275086,28053342,23776532,48376982,72802186,60393864,48713678,43161129,34061332,84988822,22371551]
}
wasm_io = {
    'g': [17487418,null,29900110,null,null,24376384,5343970,null,8403199,17899830,14572231,null,6868628,null,null,3170442],
    'o': [94028193,2696202,276042864,123686050,57783636,277630182,26520674,26713890,67126406,94213263,87363049,30898671,58847728,43152489,160183427,24542432],
    'p': [65485419,null,221279548,83899616,40320456,197894846,26862173,28976812,58168022,66547724,64727800,null,46451450,35278113,88830918,25176872]
}


category_colors = plt.get_cmap('Paired')(np.linspace(0.15, 0.85, 5))
plt.switch_backend('TkAgg')
fig, ax = plt.subplots(figsize=(16, 6))
width = 0.25  # the width of the bars

x = np.arange(len(contracts[:-2]))  # the label locations

clients = {'g': 'Geth', 'o': 'Openethereum', 'p': 'PlatON-Go'}

for i, (client_code, client_name) in enumerate(clients.items()):
    bars = ax.bar(x + i * width, [(wasm_io[client_code][j] / evm_io[client_code][j] if wasm_io[client_code][j] / evm_io[client_code][j] > 1. else 1.05) for j in x],
                  width, label=client_name, color=category_colors[i],bottom = 0)
    # for bar in bars:
    #     height = bar.get_height()
    #     if height == 0:
    #         continue
    #     ax.text(bar.get_x() + bar.get_width() / 2., height,
    #             '%0.2f' % height, ha='center', va='bottom', fontsize=7)

# ax.set_xlabel('合约名', {'family': 'SimSun', 'weight': 'normal', 'size': 20})
ax.set_ylabel('IO(Wasm)/IO(EVM)', {'family': 'consolas', 'weight': 'normal', 'size': 15})
ax.set_xticks(x + width)
ax.set_xticklabels(contracts[:-2], rotation=30, fontsize=15,position = (0,0.01))
ax.legend()

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

legend = ax.legend(loc='upper right',bbox_to_anchor = (0.85,0.9),fontsize=11)

# plt.title('合约字节码长度比例')
plt.tight_layout()
plt.savefig('./fig/io.pdf', dpi=600, bbox_inches='tight')
plt.show()
