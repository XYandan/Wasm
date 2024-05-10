import matplotlib.pyplot as plt
import numpy as np

plt.rc('font', family='consolas')

null = 0

contracts = ['bit','contract','erc20','forwarder','gambling','global','hash','invoke','map','math','memory','proxy','storage','transfer','wallet','null','null_f']
evm_deploy_gas = {
    'g': [184443,142069,432500,428523,398708,209077,134483,126713,110801,199947,335037,291996,107165,115835,289849,68990,86047],
    'o': [149515,142069,432500,428523,405542,209077,134483,126713,110801,161121,335037,291996,107165,115835,289849,68990,86047],
    'p': [89351,81589,219200,189663,210788,103237,79223,75593,71561,93125,125678,130716,73865,73175,145309,59270,63547]
}
wasm_deploy_gas = {
    'g': [1032157,null,4151749,null,null,1099385,482457,null,809521,1552749,3891409,null,515585,408525,null,88717,160357],
    'o': [2954236,2032364,4791536,3870601,4122873,2376448,2247332,1427134,2552004,3102480,2555488,2687112,1926103,1507962,3253258,869055,1017331],
    'p': [102947,null,246778,191527,209434,113429,96927,106195,149701,107498,96214,null,106268,91195,159369,81717,83123]
}


category_colors = plt.get_cmap('Paired')(np.linspace(0.15, 0.85, 5))
plt.switch_backend('TkAgg')
fig, ax = plt.subplots(figsize=(16, 6))
width = 0.25  # the width of the bars

x = np.arange(len(contracts[:-2]))  # the label locations

clients = {'g': 'Geth', 'o': 'Openethereum', 'p': 'PlatON-Go'}

for i, (client_code, client_name) in enumerate(clients.items()):
    bars = ax.bar(x + i * width, [wasm_deploy_gas[client_code][j] / evm_deploy_gas[client_code][j] for j in x],
                  width, label=client_name, color=category_colors[i],bottom = 0)
    for bar in bars:
        height = bar.get_height()
        if height == 0:
            continue
        ax.text(bar.get_x() + bar.get_width() / 2., height,
                '%0.2f' % height, ha='center', va='bottom', fontsize=7)

ax.set_xlabel('合约名', {'family': 'SimSun', 'weight': 'normal', 'size': 25})
ax.set_ylabel('合约部署消耗Gas比例', {'family': 'SimSun', 'weight': 'normal', 'size': 25})
ax.set_xticks(x + width)
ax.set_xticklabels(contracts[:-2], rotation=45, fontsize=20)
ax.legend()

legend = ax.legend(fontsize=16)

# plt.title('合约字节码长度比例')
plt.tight_layout()
plt.savefig('deploy_six_tot.pdf', dpi=600, bbox_inches='tight')
plt.show()
