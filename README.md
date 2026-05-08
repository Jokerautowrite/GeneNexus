# GeneNexus

> 璇玑基因枢纽 · 智能体进化熔炉

**GeneNexus** — 连接璇玑基因库与智能体SKILL的枢纽

---

## APEX V10 主公式

```
ΔG_final = (C_total × Λ_gene × Ω_entropy × Φ_all × Θ_bio) / (H_info × t)
```

### 核心子公式

#### 全能融合 Φ_all

```
Φ_all = (K × H × P × ΔR × S_p) / (N × τ)
```

#### 生物调控 Θ_bio

```
Θ_bio = (EMF × Ca²⁺ × Gene_reg) / (Loss_bio × τ)
```

---

## 核心定位

解决璇玑基因无法直接注入智能体的难题：
```
璇玑基因库 → GeneNexus → SKILL格式 → 墨羽学会
```

---

## 工作流程

```
┌─────────────────┐
│  璇玑基因库     │
│  /nvm/assets/   │
└────────┬────────┘
         │ GeneNexus读取
         ▼
┌─────────────────┐
│  策略提取器     │
│  strategy_      │
│  extractor.py   │
└────────┬────────┘
         │ 策略格式化
         ▼
┌─────────────────┐
│  SKILL生成器    │
│  skill_generator│
│  .py            │
└────────┬────────┘
         │ 墨羽学习
         ▼
┌─────────────────┐
│  墨羽技能库     │
│  SKILL/        │
└─────────────────┘
```

---

## 核心模块

### 1. 基因读取器
```python
from gene_nexus import GeneReader

reader = GeneReader("/root/.nvm/assets/gep/genes.json")
genes = reader.load_genes()
print(f"加载 {len(genes)} 个基因")
```

### 2. 策略提取器
```python
from gene_nexus import StrategyExtractor

extractor = StrategyExtractor()
for gene in genes:
    strategy = extractor.extract(gene)
    print(f"策略: {strategy}")
```

### 3. SKILL生成器
```python
from gene_nexus import SkillGenerator

generator = SkillGenerator()
skill = generator.generate(strategy)
print(f"SKILL: {skill.name}")
```

---

## 安装

```bash
git clone https://github.com/ApexSpiral/GeneNexus.git
cd GeneNexus
pip install -r requirements.txt
```

---

## 测试

```bash
pytest tests/ -v
```

---

## V10 特性

- ✅ V10主公式+双翼闭环
- ✅ Φ_all全能融合
- ✅ Θ_bio生物调控
- ✅ 连接璇玑基因与SKILL

---

## License

MIT
