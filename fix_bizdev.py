import re
with open('.opencode/rules/biz-dev-rules.md', 'r') as f:
    content = f.read()
dev_pattern = r'- \*\*开发向内求解 \(Inward Solving First\)\*\*：解决问题时的出发点和首选方向是“向内求解”。遇到 Bug 或编排失败时，第一反应必须是审查并修改项目自身的业务代码或逻辑结构。只有在确信业务代码本身逻辑严密、完美无缺后，才允许“向外求解”，去排查是否是外部运行环境、系统级配置出现了故障。严禁一开始就通过修改外部环境来掩盖残缺的代码。'
dev_replacement = r'- **诊因只向事实，求解向内优先 (Factual Diagnosis, Inward Solving First)**：诊断根因时必须保持客观，只向事实。但在**求解（寻求解决方案）**时，出发点和首选方向是“向内求解”。首选原生方案是审查并修改项目自身的业务代码或逻辑结构。只有在确定业务代码本身逻辑完美无缺，或者确认修改代码无法解决该问题后，才允许“向外求解”（排查外部运行环境、系统级配置是否有故障）。严禁通过非原生、扭曲的外部环境配置来掩盖残缺的代码。'
new_content = content.replace(dev_pattern, dev_replacement)
with open('.opencode/rules/biz-dev-rules.md', 'w') as f:
    f.write(new_content)
