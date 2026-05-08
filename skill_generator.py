"""SKILL格式生成器 - 生成墨羽可学习的SKILL"""
from typing import Dict, List
from datetime import datetime


class SkillGenerator:
    """生成SKILL.md格式"""
    
    def generate(self, strategy: Dict) -> str:
        """生成SKILL.md内容"""
        name = strategy.get('name', 'unknown')
        content = f"""# SKILL - {name}

## 描述
{strategy.get('strategy', '无描述')}

## 来源
- 基因名称: {name}
- 适应度: {strategy.get('fitness', 0.0)}

## 参数
{self._format_params(strategy.get('parameters', {}))}

## 使用场景
适用本SKILL的典型场景说明。

## 使用方法
```python
# 示例代码
```

## 注意事项
- 使用前请确认参数
- 适合的场景：{name}
"""
        return content
    
    def _format_params(self, params: Dict) -> str:
        """格式化参数"""
        if not params:
            return "无特定参数"
        return "\n".join([f"- {k}: {v}" for k, v in params.items()])
