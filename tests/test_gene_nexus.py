"""GeneNexus测试"""
import pytest
from gene_nexus import GeneReader, StrategyExtractor, SkillGenerator


class TestGeneReader:
    def test_load_genes(self):
        reader = GeneReader()
        genes = reader.load_genes()
        assert isinstance(genes, list)
    
    def test_get_gene_by_name(self):
        reader = GeneReader()
        gene = reader.get_gene_by_name("test")
        # 即使找不到也不报错
        assert gene is None or isinstance(gene, dict)


class TestStrategyExtractor:
    def test_extract(self):
        extractor = StrategyExtractor()
        result = extractor.extract({'name': 'test', 'fitness': 1.0})
        assert result['name'] == 'test'
        assert result['fitness'] == 1.0


class TestSkillGenerator:
    def test_generate(self):
        generator = SkillGenerator()
        content = generator.generate({'name': 'test', 'strategy': 'test strategy'})
        assert 'test' in content
        assert 'SKILL' in content
