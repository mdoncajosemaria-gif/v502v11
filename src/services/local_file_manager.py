#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ARQV30 Enhanced v2.0 - Local File Manager
Gerenciador para salvamento local de análises em arquivos TXT separados
"""

import os
import logging
import json
from typing import Dict, List, Any, Optional
from datetime import datetime
import uuid

logger = logging.getLogger(__name__)

class LocalFileManager:
    """Gerenciador de arquivos locais para análises"""
    
    def __init__(self):
        """Inicializa o gerenciador de arquivos locais"""
        self.base_dir = os.path.join(os.path.dirname(__file__), '..', 'analyses_output')
        self.ensure_directories()
        
        logger.info(f"✅ Local File Manager inicializado - Diretório: {self.base_dir}")
    
    def ensure_directories(self):
        """Garante que os diretórios necessários existam"""
        directories = [
            self.base_dir,
            os.path.join(self.base_dir, 'avatars'),
            os.path.join(self.base_dir, 'drivers_mentais'),
            os.path.join(self.base_dir, 'provas_visuais'),
            os.path.join(self.base_dir, 'anti_objecao'),
            os.path.join(self.base_dir, 'pre_pitch'),
            os.path.join(self.base_dir, 'predicoes_futuro'),
            os.path.join(self.base_dir, 'posicionamento'),
            os.path.join(self.base_dir, 'concorrencia'),
            os.path.join(self.base_dir, 'palavras_chave'),
            os.path.join(self.base_dir, 'metricas'),
            os.path.join(self.base_dir, 'funil_vendas'),
            os.path.join(self.base_dir, 'plano_acao'),
            os.path.join(self.base_dir, 'insights'),
            os.path.join(self.base_dir, 'pesquisa_web'),
            os.path.join(self.base_dir, 'completas'),
            os.path.join(self.base_dir, 'metadata')
        ]
        
        for directory in directories:
            os.makedirs(directory, exist_ok=True)
    
    def save_analysis_locally(self, analysis_data: Dict[str, Any], analysis_id: Optional[str] = None) -> Dict[str, Any]:
        """Salva análise completa em arquivos TXT separados"""
        
        if not analysis_id:
            analysis_id = str(uuid.uuid4())
        
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        segmento = analysis_data.get('segmento', 'sem_segmento').replace(' ', '_').lower()
        
        # Prefixo para todos os arquivos
        file_prefix = f"{timestamp}_{segmento}_{analysis_id[:8]}"
        
        saved_files = []
        
        try:
            # 1. AVATAR ULTRA-DETALHADO
            if analysis_data.get('avatar_ultra_detalhado'):
                file_path = self._save_avatar_file(
                    analysis_data['avatar_ultra_detalhado'], 
                    file_prefix
                )
                if file_path:
                    saved_files.append({
                        'type': 'avatar',
                        'name': os.path.basename(file_path),
                        'path': file_path,
                        'size': os.path.getsize(file_path)
                    })
            
            # 2. DRIVERS MENTAIS CUSTOMIZADOS
            if analysis_data.get('drivers_mentais_customizados'):
                file_path = self._save_drivers_file(
                    analysis_data['drivers_mentais_customizados'], 
                    file_prefix
                )
                if file_path:
                    saved_files.append({
                        'type': 'drivers_mentais',
                        'name': os.path.basename(file_path),
                        'path': file_path,
                        'size': os.path.getsize(file_path)
                    })
            
            # 3. PROVAS VISUAIS INSTANTÂNEAS
            if analysis_data.get('provas_visuais_instantaneas'):
                file_path = self._save_provas_file(
                    analysis_data['provas_visuais_instantaneas'], 
                    file_prefix
                )
                if file_path:
                    saved_files.append({
                        'type': 'provas_visuais',
                        'name': os.path.basename(file_path),
                        'path': file_path,
                        'size': os.path.getsize(file_path)
                    })
            
            # 4. SISTEMA ANTI-OBJEÇÃO
            if analysis_data.get('sistema_anti_objecao'):
                file_path = self._save_anti_objecao_file(
                    analysis_data['sistema_anti_objecao'], 
                    file_prefix
                )
                if file_path:
                    saved_files.append({
                        'type': 'anti_objecao',
                        'name': os.path.basename(file_path),
                        'path': file_path,
                        'size': os.path.getsize(file_path)
                    })
            
            # 5. PRÉ-PITCH INVISÍVEL
            if analysis_data.get('pre_pitch_invisivel'):
                file_path = self._save_pre_pitch_file(
                    analysis_data['pre_pitch_invisivel'], 
                    file_prefix
                )
                if file_path:
                    saved_files.append({
                        'type': 'pre_pitch',
                        'name': os.path.basename(file_path),
                        'path': file_path,
                        'size': os.path.getsize(file_path)
                    })
            
            # 6. PREDIÇÕES DO FUTURO
            if analysis_data.get('predicoes_futuro_completas'):
                file_path = self._save_predicoes_file(
                    analysis_data['predicoes_futuro_completas'], 
                    file_prefix
                )
                if file_path:
                    saved_files.append({
                        'type': 'predicoes_futuro',
                        'name': os.path.basename(file_path),
                        'path': file_path,
                        'size': os.path.getsize(file_path)
                    })
            
            # 7. POSICIONAMENTO E ESCOPO
            if analysis_data.get('escopo'):
                file_path = self._save_posicionamento_file(
                    analysis_data['escopo'], 
                    file_prefix
                )
                if file_path:
                    saved_files.append({
                        'type': 'posicionamento',
                        'name': os.path.basename(file_path),
                        'path': file_path,
                        'size': os.path.getsize(file_path)
                    })
            
            # 8. ANÁLISE DE CONCORRÊNCIA
            if analysis_data.get('analise_concorrencia_detalhada'):
                file_path = self._save_concorrencia_file(
                    analysis_data['analise_concorrencia_detalhada'], 
                    file_prefix
                )
                if file_path:
                    saved_files.append({
                        'type': 'concorrencia',
                        'name': os.path.basename(file_path),
                        'path': file_path,
                        'size': os.path.getsize(file_path)
                    })
            
            # 9. ESTRATÉGIA DE PALAVRAS-CHAVE
            if analysis_data.get('estrategia_palavras_chave'):
                file_path = self._save_palavras_chave_file(
                    analysis_data['estrategia_palavras_chave'], 
                    file_prefix
                )
                if file_path:
                    saved_files.append({
                        'type': 'palavras_chave',
                        'name': os.path.basename(file_path),
                        'path': file_path,
                        'size': os.path.getsize(file_path)
                    })
            
            # 10. MÉTRICAS DE PERFORMANCE
            if analysis_data.get('metricas_performance_detalhadas'):
                file_path = self._save_metricas_file(
                    analysis_data['metricas_performance_detalhadas'], 
                    file_prefix
                )
                if file_path:
                    saved_files.append({
                        'type': 'metricas',
                        'name': os.path.basename(file_path),
                        'path': file_path,
                        'size': os.path.getsize(file_path)
                    })
            
            # 11. FUNIL DE VENDAS
            if analysis_data.get('funil_vendas_detalhado'):
                file_path = self._save_funil_file(
                    analysis_data['funil_vendas_detalhado'], 
                    file_prefix
                )
                if file_path:
                    saved_files.append({
                        'type': 'funil_vendas',
                        'name': os.path.basename(file_path),
                        'path': file_path,
                        'size': os.path.getsize(file_path)
                    })
            
            # 12. PLANO DE AÇÃO
            if analysis_data.get('plano_acao_detalhado'):
                file_path = self._save_plano_acao_file(
                    analysis_data['plano_acao_detalhado'], 
                    file_prefix
                )
                if file_path:
                    saved_files.append({
                        'type': 'plano_acao',
                        'name': os.path.basename(file_path),
                        'path': file_path,
                        'size': os.path.getsize(file_path)
                    })
            
            # 13. INSIGHTS EXCLUSIVOS
            if analysis_data.get('insights_exclusivos'):
                file_path = self._save_insights_file(
                    analysis_data['insights_exclusivos'], 
                    file_prefix
                )
                if file_path:
                    saved_files.append({
                        'type': 'insights',
                        'name': os.path.basename(file_path),
                        'path': file_path,
                        'size': os.path.getsize(file_path)
                    })
            
            # 14. PESQUISA WEB MASSIVA
            if analysis_data.get('pesquisa_web_massiva'):
                file_path = self._save_pesquisa_web_file(
                    analysis_data['pesquisa_web_massiva'], 
                    file_prefix
                )
                if file_path:
                    saved_files.append({
                        'type': 'pesquisa_web',
                        'name': os.path.basename(file_path),
                        'path': file_path,
                        'size': os.path.getsize(file_path)
                    })
            
            # 15. ANÁLISE COMPLETA (JSON)
            file_path = self._save_complete_analysis_file(analysis_data, file_prefix)
            if file_path:
                saved_files.append({
                    'type': 'completa',
                    'name': os.path.basename(file_path),
                    'path': file_path,
                    'size': os.path.getsize(file_path)
                })
            
            # 16. METADATA
            metadata = {
                'analysis_id': analysis_id,
                'timestamp': timestamp,
                'segmento': segmento,
                'total_files': len(saved_files),
                'files': saved_files,
                'generated_at': datetime.now().isoformat()
            }
            
            metadata_path = self._save_metadata_file(metadata, file_prefix)
            if metadata_path:
                saved_files.append({
                    'type': 'metadata',
                    'name': os.path.basename(metadata_path),
                    'path': metadata_path,
                    'size': os.path.getsize(metadata_path)
                })
            
            logger.info(f"✅ Análise salva localmente: {len(saved_files)} arquivos criados")
            
            return {
                'success': True,
                'analysis_id': analysis_id,
                'files_created': len(saved_files),
                'files': saved_files,
                'base_directory': self.base_dir,
                'total_size': sum(f['size'] for f in saved_files)
            }
            
        except Exception as e:
            logger.error(f"❌ Erro ao salvar análise localmente: {str(e)}")
            return {
                'success': False,
                'error': str(e),
                'files': saved_files  # Arquivos que conseguiu salvar
            }
    
    def _save_avatar_file(self, avatar_data: Dict[str, Any], file_prefix: str) -> Optional[str]:
        """Salva dados do avatar em arquivo TXT"""
        try:
            file_path = os.path.join(self.base_dir, 'avatars', f"{file_prefix}_avatar.txt")
            
            content = "=" * 80 + "\n"
            content += "AVATAR ULTRA-DETALHADO\n"
            content += "=" * 80 + "\n\n"
            
            # Perfil Demográfico
            if avatar_data.get('perfil_demografico'):
                content += "PERFIL DEMOGRÁFICO:\n"
                content += "-" * 40 + "\n"
                for key, value in avatar_data['perfil_demografico'].items():
                    content += f"{key.replace('_', ' ').title()}: {value}\n"
                content += "\n"
            
            # Perfil Psicográfico
            if avatar_data.get('perfil_psicografico'):
                content += "PERFIL PSICOGRÁFICO:\n"
                content += "-" * 40 + "\n"
                for key, value in avatar_data['perfil_psicografico'].items():
                    content += f"{key.replace('_', ' ').title()}: {value}\n"
                content += "\n"
            
            # Dores Viscerais
            if avatar_data.get('dores_viscerais'):
                content += "DORES VISCERAIS:\n"
                content += "-" * 40 + "\n"
                for i, dor in enumerate(avatar_data['dores_viscerais'], 1):
                    content += f"{i:2d}. {dor}\n"
                content += "\n"
            
            # Desejos Secretos
            if avatar_data.get('desejos_secretos'):
                content += "DESEJOS SECRETOS:\n"
                content += "-" * 40 + "\n"
                for i, desejo in enumerate(avatar_data['desejos_secretos'], 1):
                    content += f"{i:2d}. {desejo}\n"
                content += "\n"
            
            # Objeções Reais
            if avatar_data.get('objecoes_reais'):
                content += "OBJEÇÕES REAIS:\n"
                content += "-" * 40 + "\n"
                for i, objecao in enumerate(avatar_data['objecoes_reais'], 1):
                    content += f"{i:2d}. {objecao}\n"
                content += "\n"
            
            # Jornada Emocional
            if avatar_data.get('jornada_emocional'):
                content += "JORNADA EMOCIONAL:\n"
                content += "-" * 40 + "\n"
                for key, value in avatar_data['jornada_emocional'].items():
                    content += f"{key.replace('_', ' ').title()}: {value}\n"
                content += "\n"
            
            # Linguagem Interna
            if avatar_data.get('linguagem_interna'):
                content += "LINGUAGEM INTERNA:\n"
                content += "-" * 40 + "\n"
                for key, value in avatar_data['linguagem_interna'].items():
                    if isinstance(value, list):
                        content += f"{key.replace('_', ' ').title()}:\n"
                        for item in value:
                            content += f"  • {item}\n"
                    else:
                        content += f"{key.replace('_', ' ').title()}: {value}\n"
                content += "\n"
            
            content += f"\nGerado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            logger.info(f"✅ Avatar salvo: {file_path}")
            return file_path
            
        except Exception as e:
            logger.error(f"❌ Erro ao salvar avatar: {str(e)}")
            return None
    
    def _save_drivers_file(self, drivers_data: Dict[str, Any], file_prefix: str) -> Optional[str]:
        """Salva drivers mentais em arquivo TXT"""
        try:
            file_path = os.path.join(self.base_dir, 'drivers_mentais', f"{file_prefix}_drivers.txt")
            
            content = "=" * 80 + "\n"
            content += "DRIVERS MENTAIS CUSTOMIZADOS\n"
            content += "=" * 80 + "\n\n"
            
            # Drivers Customizados
            if drivers_data.get('drivers_customizados'):
                for i, driver in enumerate(drivers_data['drivers_customizados'], 1):
                    content += f"DRIVER {i}: {driver.get('nome', 'Driver Mental')}\n"
                    content += "-" * 60 + "\n"
                    content += f"Gatilho Central: {driver.get('gatilho_central', 'N/A')}\n"
                    content += f"Definição: {driver.get('definicao_visceral', 'N/A')}\n"
                    
                    if driver.get('roteiro_ativacao'):
                        content += "\nRoteiro de Ativação:\n"
                        roteiro = driver['roteiro_ativacao']
                        content += f"  Pergunta: {roteiro.get('pergunta_abertura', 'N/A')}\n"
                        content += f"  História: {roteiro.get('historia_analogia', 'N/A')}\n"
                        content += f"  Comando: {roteiro.get('comando_acao', 'N/A')}\n"
                    
                    if driver.get('frases_ancoragem'):
                        content += "\nFrases de Ancoragem:\n"
                        for frase in driver['frases_ancoragem']:
                            content += f"  • \"{frase}\"\n"
                    
                    content += "\n" + "=" * 60 + "\n\n"
            
            # Sequenciamento Estratégico
            if drivers_data.get('sequenciamento_estrategico'):
                content += "SEQUENCIAMENTO ESTRATÉGICO:\n"
                content += "-" * 40 + "\n"
                for fase, dados in drivers_data['sequenciamento_estrategico'].items():
                    content += f"{fase.replace('_', ' ').title()}:\n"
                    content += f"  Objetivo: {dados.get('objetivo', 'N/A')}\n"
                    content += f"  Duração: {dados.get('duracao', 'N/A')}\n"
                    content += f"  Drivers: {', '.join(dados.get('drivers', []))}\n\n"
            
            content += f"\nGerado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            logger.info(f"✅ Drivers mentais salvos: {file_path}")
            return file_path
            
        except Exception as e:
            logger.error(f"❌ Erro ao salvar drivers mentais: {str(e)}")
            return None
    
    def _save_provas_file(self, provas_data: List[Dict[str, Any]], file_prefix: str) -> Optional[str]:
        """Salva provas visuais em arquivo TXT"""
        try:
            file_path = os.path.join(self.base_dir, 'provas_visuais', f"{file_prefix}_provas.txt")
            
            content = "=" * 80 + "\n"
            content += "PROVAS VISUAIS INSTANTÂNEAS\n"
            content += "=" * 80 + "\n\n"
            
            for i, prova in enumerate(provas_data, 1):
                content += f"PROVA {i}: {prova.get('nome', 'Prova Visual')}\n"
                content += "-" * 60 + "\n"
                content += f"Conceito Alvo: {prova.get('conceito_alvo', 'N/A')}\n"
                content += f"Experimento: {prova.get('experimento', 'N/A')}\n"
                
                if prova.get('materiais'):
                    content += "\nMateriais Necessários:\n"
                    for material in prova['materiais']:
                        content += f"  • {material}\n"
                
                if prova.get('roteiro_completo'):
                    content += f"\nRoteiro Completo:\n{prova['roteiro_completo']}\n"
                
                if prova.get('impacto_esperado'):
                    content += f"\nImpacto Esperado: {prova['impacto_esperado']}\n"
                
                content += "\n" + "=" * 60 + "\n\n"
            
            content += f"\nGerado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            logger.info(f"✅ Provas visuais salvas: {file_path}")
            return file_path
            
        except Exception as e:
            logger.error(f"❌ Erro ao salvar provas visuais: {str(e)}")
            return None
    
    def _save_anti_objecao_file(self, anti_objecao_data: Dict[str, Any], file_prefix: str) -> Optional[str]:
        """Salva sistema anti-objeção em arquivo TXT"""
        try:
            file_path = os.path.join(self.base_dir, 'anti_objecao', f"{file_prefix}_anti_objecao.txt")
            
            content = "=" * 80 + "\n"
            content += "SISTEMA ANTI-OBJEÇÃO\n"
            content += "=" * 80 + "\n\n"
            
            # Objeções Universais
            if anti_objecao_data.get('objecoes_universais'):
                content += "OBJEÇÕES UNIVERSAIS:\n"
                content += "-" * 40 + "\n"
                for tipo, objecao in anti_objecao_data['objecoes_universais'].items():
                    content += f"{tipo.upper()}:\n"
                    if isinstance(objecao, dict):
                        content += f"  Objeção: {objecao.get('objecao', 'N/A')}\n"
                        content += f"  Contra-ataque: {objecao.get('contra_ataque', 'N/A')}\n"
                        if objecao.get('scripts_customizados'):
                            content += "  Scripts:\n"
                            for script in objecao['scripts_customizados']:
                                content += f"    • {script}\n"
                    content += "\n"
            
            # Objeções Ocultas
            if anti_objecao_data.get('objecoes_ocultas'):
                content += "OBJEÇÕES OCULTAS:\n"
                content += "-" * 40 + "\n"
                for tipo, objecao in anti_objecao_data['objecoes_ocultas'].items():
                    content += f"{tipo.replace('_', ' ').upper()}:\n"
                    if isinstance(objecao, dict):
                        content += f"  Perfil: {objecao.get('perfil_tipico', 'N/A')}\n"
                        content += f"  Contra-ataque: {objecao.get('contra_ataque', 'N/A')}\n"
                    content += "\n"
            
            # Scripts Personalizados
            if anti_objecao_data.get('scripts_personalizados'):
                content += "SCRIPTS PERSONALIZADOS:\n"
                content += "-" * 40 + "\n"
                for categoria, scripts in anti_objecao_data['scripts_personalizados'].items():
                    content += f"{categoria.replace('_', ' ').upper()}:\n"
                    if isinstance(scripts, list):
                        for script in scripts:
                            content += f"  • {script}\n"
                    content += "\n"
            
            content += f"\nGerado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            logger.info(f"✅ Sistema anti-objeção salvo: {file_path}")
            return file_path
            
        except Exception as e:
            logger.error(f"❌ Erro ao salvar sistema anti-objeção: {str(e)}")
            return None
    
    def _save_pre_pitch_file(self, pre_pitch_data: Dict[str, Any], file_prefix: str) -> Optional[str]:
        """Salva pré-pitch invisível em arquivo TXT"""
        try:
            file_path = os.path.join(self.base_dir, 'pre_pitch', f"{file_prefix}_pre_pitch.txt")
            
            content = "=" * 80 + "\n"
            content += "PRÉ-PITCH INVISÍVEL\n"
            content += "=" * 80 + "\n\n"
            
            # Orquestração Emocional
            if pre_pitch_data.get('orquestracao_emocional'):
                content += "ORQUESTRAÇÃO EMOCIONAL:\n"
                content += "-" * 40 + "\n"
                
                sequencia = pre_pitch_data['orquestracao_emocional'].get('sequencia_psicologica', [])
                for fase in sequencia:
                    content += f"Fase: {fase.get('fase', 'N/A')}\n"
                    content += f"  Objetivo: {fase.get('objetivo', 'N/A')}\n"
                    content += f"  Duração: {fase.get('duracao', 'N/A')}\n"
                    content += f"  Intensidade: {fase.get('intensidade', 'N/A')}\n"
                    if fase.get('tecnicas'):
                        content += f"  Técnicas: {', '.join(fase['tecnicas'])}\n"
                    content += "\n"
            
            # Roteiro Completo
            if pre_pitch_data.get('roteiro_completo'):
                content += "ROTEIRO COMPLETO:\n"
                content += "-" * 40 + "\n"
                roteiro = pre_pitch_data['roteiro_completo']
                
                for secao, dados in roteiro.items():
                    content += f"{secao.replace('_', ' ').upper()}:\n"
                    if isinstance(dados, dict):
                        for key, value in dados.items():
                            content += f"  {key.replace('_', ' ').title()}: {value}\n"
                    content += "\n"
            
            content += f"\nGerado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            logger.info(f"✅ Pré-pitch salvo: {file_path}")
            return file_path
            
        except Exception as e:
            logger.error(f"❌ Erro ao salvar pré-pitch: {str(e)}")
            return None
    
    def _save_predicoes_file(self, predicoes_data: Dict[str, Any], file_prefix: str) -> Optional[str]:
        """Salva predições do futuro em arquivo TXT"""
        try:
            file_path = os.path.join(self.base_dir, 'predicoes_futuro', f"{file_prefix}_predicoes.txt")
            
            content = "=" * 80 + "\n"
            content += "PREDIÇÕES DO FUTURO\n"
            content += "=" * 80 + "\n\n"
            
            # Tendências Atuais
            if predicoes_data.get('tendencias_atuais'):
                content += "TENDÊNCIAS ATUAIS:\n"
                content += "-" * 40 + "\n"
                
                tendencias = predicoes_data['tendencias_atuais']
                if tendencias.get('tendencias_relevantes'):
                    for trend_name, trend_data in tendencias['tendencias_relevantes'].items():
                        content += f"{trend_name.upper()}:\n"
                        content += f"  Fase: {trend_data.get('fase_atual', 'N/A')}\n"
                        content += f"  Impacto: {trend_data.get('impacto_esperado', 'N/A')}\n"
                        content += f"  Timeline: {trend_data.get('timeline', 'N/A')}\n\n"
            
            # Cenários Futuros
            if predicoes_data.get('cenarios_futuros'):
                content += "CENÁRIOS FUTUROS:\n"
                content += "-" * 40 + "\n"
                
                for scenario_name, scenario_data in predicoes_data['cenarios_futuros'].items():
                    content += f"{scenario_data.get('nome', scenario_name).upper()}:\n"
                    content += f"  Probabilidade: {scenario_data.get('probabilidade', 'N/A')}\n"
                    content += f"  Descrição: {scenario_data.get('descricao', 'N/A')}\n"
                    if scenario_data.get('oportunidades'):
                        content += "  Oportunidades:\n"
                        for opp in scenario_data['oportunidades']:
                            content += f"    • {opp}\n"
                    content += "\n"
            
            # Oportunidades Emergentes
            if predicoes_data.get('oportunidades_emergentes'):
                content += "OPORTUNIDADES EMERGENTES:\n"
                content += "-" * 40 + "\n"
                
                for opp in predicoes_data['oportunidades_emergentes']:
                    if isinstance(opp, dict):
                        content += f"{opp.get('nome', 'Oportunidade')}:\n"
                        content += f"  Potencial: {opp.get('potencial_mercado', 'N/A')}\n"
                        content += f"  Timeline: {opp.get('timeline', 'N/A')}\n"
                        content += f"  Investimento: {opp.get('investimento_necessario', 'N/A')}\n"
                        content += f"  ROI: {opp.get('roi_esperado', 'N/A')}\n"
                    else:
                        content += f"• {opp}\n"
                    content += "\n"
            
            content += f"\nGerado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            logger.info(f"✅ Predições do futuro salvas: {file_path}")
            return file_path
            
        except Exception as e:
            logger.error(f"❌ Erro ao salvar predições: {str(e)}")
            return None
    
    def _save_posicionamento_file(self, escopo_data: Dict[str, Any], file_prefix: str) -> Optional[str]:
        """Salva dados de posicionamento em arquivo TXT"""
        try:
            file_path = os.path.join(self.base_dir, 'posicionamento', f"{file_prefix}_posicionamento.txt")
            
            content = "=" * 80 + "\n"
            content += "ESCOPO E POSICIONAMENTO\n"
            content += "=" * 80 + "\n\n"
            
            # Posicionamento no mercado
            if escopo_data.get('posicionamento_mercado'):
                content += "POSICIONAMENTO NO MERCADO:\n"
                content += "-" * 40 + "\n"
                content += f"{escopo_data['posicionamento_mercado']}\n\n"
            
            # Proposta de valor
            if escopo_data.get('proposta_valor'):
                content += "PROPOSTA DE VALOR:\n"
                content += "-" * 40 + "\n"
                content += f"{escopo_data['proposta_valor']}\n\n"
            
            # Diferenciais competitivos
            if escopo_data.get('diferenciais_competitivos'):
                content += "DIFERENCIAIS COMPETITIVOS:\n"
                content += "-" * 40 + "\n"
                for i, diferencial in enumerate(escopo_data['diferenciais_competitivos'], 1):
                    content += f"{i:2d}. {diferencial}\n"
                content += "\n"
            
            # Mensagem central
            if escopo_data.get('mensagem_central'):
                content += "MENSAGEM CENTRAL:\n"
                content += "-" * 40 + "\n"
                content += f"{escopo_data['mensagem_central']}\n\n"
            
            # Estratégia oceano azul
            if escopo_data.get('estrategia_oceano_azul'):
                content += "ESTRATÉGIA OCEANO AZUL:\n"
                content += "-" * 40 + "\n"
                content += f"{escopo_data['estrategia_oceano_azul']}\n\n"
            
            content += f"\nGerado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            logger.info(f"✅ Posicionamento salvo: {file_path}")
            return file_path
            
        except Exception as e:
            logger.error(f"❌ Erro ao salvar posicionamento: {str(e)}")
            return None
    
    def _save_concorrencia_file(self, concorrencia_data: List[Dict[str, Any]], file_prefix: str) -> Optional[str]:
        """Salva análise de concorrência em arquivo TXT"""
        try:
            file_path = os.path.join(self.base_dir, 'concorrencia', f"{file_prefix}_concorrencia.txt")
            
            content = "=" * 80 + "\n"
            content += "ANÁLISE DE CONCORRÊNCIA DETALHADA\n"
            content += "=" * 80 + "\n\n"
            
            for i, concorrente in enumerate(concorrencia_data, 1):
                content += f"CONCORRENTE {i}: {concorrente.get('nome', 'Concorrente')}\n"
                content += "-" * 60 + "\n"
                
                # Análise SWOT
                if concorrente.get('analise_swot'):
                    swot = concorrente['analise_swot']
                    content += "ANÁLISE SWOT:\n"
                    
                    if swot.get('forcas'):
                        content += "  Forças:\n"
                        for forca in swot['forcas']:
                            content += f"    • {forca}\n"
                    
                    if swot.get('fraquezas'):
                        content += "  Fraquezas:\n"
                        for fraqueza in swot['fraquezas']:
                            content += f"    • {fraqueza}\n"
                    
                    if swot.get('oportunidades'):
                        content += "  Oportunidades:\n"
                        for oportunidade in swot['oportunidades']:
                            content += f"    • {oportunidade}\n"
                    
                    if swot.get('ameacas'):
                        content += "  Ameaças:\n"
                        for ameaca in swot['ameacas']:
                            content += f"    • {ameaca}\n"
                    content += "\n"
                
                # Estratégia de marketing
                if concorrente.get('estrategia_marketing'):
                    content += f"Estratégia de Marketing: {concorrente['estrategia_marketing']}\n"
                
                # Posicionamento
                if concorrente.get('posicionamento'):
                    content += f"Posicionamento: {concorrente['posicionamento']}\n"
                
                # Vulnerabilidades
                if concorrente.get('vulnerabilidades'):
                    content += "Vulnerabilidades:\n"
                    for vuln in concorrente['vulnerabilidades']:
                        content += f"  • {vuln}\n"
                
                content += "\n" + "=" * 60 + "\n\n"
            
            content += f"\nGerado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            logger.info(f"✅ Análise de concorrência salva: {file_path}")
            return file_path
            
        except Exception as e:
            logger.error(f"❌ Erro ao salvar análise de concorrência: {str(e)}")
            return None
    
    def _save_palavras_chave_file(self, palavras_data: Dict[str, Any], file_prefix: str) -> Optional[str]:
        """Salva estratégia de palavras-chave em arquivo TXT"""
        try:
            file_path = os.path.join(self.base_dir, 'palavras_chave', f"{file_prefix}_palavras_chave.txt")
            
            content = "=" * 80 + "\n"
            content += "ESTRATÉGIA DE PALAVRAS-CHAVE\n"
            content += "=" * 80 + "\n\n"
            
            # Palavras primárias
            if palavras_data.get('palavras_primarias'):
                content += "PALAVRAS-CHAVE PRIMÁRIAS:\n"
                content += "-" * 40 + "\n"
                content += ", ".join(palavras_data['palavras_primarias']) + "\n\n"
            
            # Palavras secundárias
            if palavras_data.get('palavras_secundarias'):
                content += "PALAVRAS-CHAVE SECUNDÁRIAS:\n"
                content += "-" * 40 + "\n"
                content += ", ".join(palavras_data['palavras_secundarias']) + "\n\n"
            
            # Long tail
            if palavras_data.get('long_tail'):
                content += "PALAVRAS-CHAVE LONG TAIL:\n"
                content += "-" * 40 + "\n"
                content += ", ".join(palavras_data['long_tail']) + "\n\n"
            
            # Intenção de busca
            if palavras_data.get('intencao_busca'):
                content += "INTENÇÃO DE BUSCA:\n"
                content += "-" * 40 + "\n"
                for tipo, palavras in palavras_data['intencao_busca'].items():
                    content += f"{tipo.title()}:\n"
                    if isinstance(palavras, list):
                        content += "  " + ", ".join(palavras) + "\n"
                    content += "\n"
            
            # Estratégia de conteúdo
            if palavras_data.get('estrategia_conteudo'):
                content += "ESTRATÉGIA DE CONTEÚDO:\n"
                content += "-" * 40 + "\n"
                content += f"{palavras_data['estrategia_conteudo']}\n\n"
            
            content += f"\nGerado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            logger.info(f"✅ Palavras-chave salvas: {file_path}")
            return file_path
            
        except Exception as e:
            logger.error(f"❌ Erro ao salvar palavras-chave: {str(e)}")
            return None
    
    def _save_metricas_file(self, metricas_data: Dict[str, Any], file_prefix: str) -> Optional[str]:
        """Salva métricas de performance em arquivo TXT"""
        try:
            file_path = os.path.join(self.base_dir, 'metricas', f"{file_prefix}_metricas.txt")
            
            content = "=" * 80 + "\n"
            content += "MÉTRICAS DE PERFORMANCE DETALHADAS\n"
            content += "=" * 80 + "\n\n"
            
            # KPIs principais
            if metricas_data.get('kpis_principais'):
                content += "KPIs PRINCIPAIS:\n"
                content += "-" * 40 + "\n"
                for kpi in metricas_data['kpis_principais']:
                    if isinstance(kpi, dict):
                        content += f"Métrica: {kpi.get('metrica', 'N/A')}\n"
                        content += f"  Objetivo: {kpi.get('objetivo', 'N/A')}\n"
                        content += f"  Frequência: {kpi.get('frequencia', 'N/A')}\n"
                        content += f"  Responsável: {kpi.get('responsavel', 'N/A')}\n\n"
            
            # Projeções financeiras
            if metricas_data.get('projecoes_financeiras'):
                content += "PROJEÇÕES FINANCEIRAS:\n"
                content += "-" * 40 + "\n"
                
                for cenario, dados in metricas_data['projecoes_financeiras'].items():
                    content += f"{cenario.replace('_', ' ').upper()}:\n"
                    if isinstance(dados, dict):
                        for key, value in dados.items():
                            content += f"  {key.replace('_', ' ').title()}: {value}\n"
                    content += "\n"
            
            # ROI esperado
            if metricas_data.get('roi_esperado'):
                content += f"ROI ESPERADO: {metricas_data['roi_esperado']}\n\n"
            
            # Payback
            if metricas_data.get('payback_investimento'):
                content += f"PAYBACK DO INVESTIMENTO: {metricas_data['payback_investimento']}\n\n"
            
            content += f"\nGerado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            logger.info(f"✅ Métricas salvas: {file_path}")
            return file_path
            
        except Exception as e:
            logger.error(f"❌ Erro ao salvar métricas: {str(e)}")
            return None
    
    def _save_funil_file(self, funil_data: Dict[str, Any], file_prefix: str) -> Optional[str]:
        """Salva funil de vendas em arquivo TXT"""
        try:
            file_path = os.path.join(self.base_dir, 'funil_vendas', f"{file_prefix}_funil.txt")
            
            content = "=" * 80 + "\n"
            content += "FUNIL DE VENDAS DETALHADO\n"
            content += "=" * 80 + "\n\n"
            
            fases = ['topo_funil', 'meio_funil', 'fundo_funil']
            
            for fase in fases:
                if funil_data.get(fase):
                    content += f"{fase.replace('_', ' ').upper()}:\n"
                    content += "-" * 40 + "\n"
                    
                    fase_data = funil_data[fase]
                    for key, value in fase_data.items():
                        if isinstance(value, list):
                            content += f"{key.replace('_', ' ').title()}:\n"
                            for item in value:
                                content += f"  • {item}\n"
                        else:
                            content += f"{key.replace('_', ' ').title()}: {value}\n"
                    content += "\n"
            
            content += f"\nGerado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            logger.info(f"✅ Funil de vendas salvo: {file_path}")
            return file_path
            
        except Exception as e:
            logger.error(f"❌ Erro ao salvar funil: {str(e)}")
            return None
    
    def _save_plano_acao_file(self, plano_data: Dict[str, Any], file_prefix: str) -> Optional[str]:
        """Salva plano de ação em arquivo TXT"""
        try:
            file_path = os.path.join(self.base_dir, 'plano_acao', f"{file_prefix}_plano_acao.txt")
            
            content = "=" * 80 + "\n"
            content += "PLANO DE AÇÃO DETALHADO\n"
            content += "=" * 80 + "\n\n"
            
            # Fases do plano
            fases = ['primeiros_30_dias', 'dias_31_60', 'dias_61_90', 'fase_1_preparacao', 'fase_2_lancamento', 'fase_3_crescimento']
            
            for fase in fases:
                if plano_data.get(fase):
                    content += f"{fase.replace('_', ' ').upper()}:\n"
                    content += "-" * 40 + "\n"
                    
                    fase_data = plano_data[fase]
                    for key, value in fase_data.items():
                        if isinstance(value, list):
                            content += f"{key.replace('_', ' ').title()}:\n"
                            for item in value:
                                content += f"  • {item}\n"
                        else:
                            content += f"{key.replace('_', ' ').title()}: {value}\n"
                    content += "\n"
            
            content += f"\nGerado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            logger.info(f"✅ Plano de ação salvo: {file_path}")
            return file_path
            
        except Exception as e:
            logger.error(f"❌ Erro ao salvar plano de ação: {str(e)}")
            return None
    
    def _save_insights_file(self, insights_data: List[str], file_prefix: str) -> Optional[str]:
        """Salva insights exclusivos em arquivo TXT"""
        try:
            file_path = os.path.join(self.base_dir, 'insights', f"{file_prefix}_insights.txt")
            
            content = "=" * 80 + "\n"
            content += "INSIGHTS EXCLUSIVOS\n"
            content += "=" * 80 + "\n\n"
            
            for i, insight in enumerate(insights_data, 1):
                content += f"{i:2d}. {insight}\n\n"
            
            content += f"\nTotal de insights: {len(insights_data)}\n"
            content += f"Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            logger.info(f"✅ Insights salvos: {file_path}")
            return file_path
            
        except Exception as e:
            logger.error(f"❌ Erro ao salvar insights: {str(e)}")
            return None
    
    def _save_pesquisa_web_file(self, pesquisa_data: Dict[str, Any], file_prefix: str) -> Optional[str]:
        """Salva dados da pesquisa web em arquivo TXT"""
        try:
            file_path = os.path.join(self.base_dir, 'pesquisa_web', f"{file_prefix}_pesquisa.txt")
            
            content = "=" * 80 + "\n"
            content += "PESQUISA WEB MASSIVA\n"
            content += "=" * 80 + "\n\n"
            
            # Estatísticas
            if pesquisa_data.get('estatisticas'):
                content += "ESTATÍSTICAS DA PESQUISA:\n"
                content += "-" * 40 + "\n"
                stats = pesquisa_data['estatisticas']
                for key, value in stats.items():
                    content += f"{key.replace('_', ' ').title()}: {value}\n"
                content += "\n"
            
            # Queries executadas
            if pesquisa_data.get('queries_executadas'):
                content += "QUERIES EXECUTADAS:\n"
                content += "-" * 40 + "\n"
                for i, query in enumerate(pesquisa_data['queries_executadas'], 1):
                    content += f"{i:2d}. {query}\n"
                content += "\n"
            
            # Fontes
            if pesquisa_data.get('fontes'):
                content += "FONTES CONSULTADAS:\n"
                content += "-" * 40 + "\n"
                for i, fonte in enumerate(pesquisa_data['fontes'], 1):
                    content += f"{i:2d}. {fonte.get('title', 'Sem título')}\n"
                    content += f"    URL: {fonte.get('url', 'N/A')}\n\n"
            
            content += f"\nGerado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            logger.info(f"✅ Pesquisa web salva: {file_path}")
            return file_path
            
        except Exception as e:
            logger.error(f"❌ Erro ao salvar pesquisa web: {str(e)}")
            return None
    
    def _save_complete_analysis_file(self, analysis_data: Dict[str, Any], file_prefix: str) -> Optional[str]:
        """Salva análise completa em arquivo JSON"""
        try:
            file_path = os.path.join(self.base_dir, 'completas', f"{file_prefix}_completa.json")
            
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(analysis_data, f, ensure_ascii=False, indent=2)
            
            logger.info(f"✅ Análise completa salva: {file_path}")
            return file_path
            
        except Exception as e:
            logger.error(f"❌ Erro ao salvar análise completa: {str(e)}")
            return None
    
    def _save_metadata_file(self, metadata: Dict[str, Any], file_prefix: str) -> Optional[str]:
        """Salva metadata em arquivo TXT"""
        try:
            file_path = os.path.join(self.base_dir, 'metadata', f"{file_prefix}_metadata.txt")
            
            content = "=" * 80 + "\n"
            content += "METADATA DA ANÁLISE\n"
            content += "=" * 80 + "\n\n"
            
            content += f"ID da Análise: {metadata['analysis_id']}\n"
            content += f"Timestamp: {metadata['timestamp']}\n"
            content += f"Segmento: {metadata['segmento']}\n"
            content += f"Total de Arquivos: {metadata['total_files']}\n"
            content += f"Gerado em: {metadata['generated_at']}\n\n"
            
            content += "ARQUIVOS CRIADOS:\n"
            content += "-" * 40 + "\n"
            for arquivo in metadata['files']:
                content += f"• {arquivo['name']} ({arquivo['type']}) - {arquivo['size']} bytes\n"
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            logger.info(f"✅ Metadata salva: {file_path}")
            return file_path
            
        except Exception as e:
            logger.error(f"❌ Erro ao salvar metadata: {str(e)}")
            return None
    
    def get_analysis_directory(self, analysis_id: str) -> Optional[str]:
        """Retorna diretório de uma análise específica"""
        # Busca por arquivos que contenham o analysis_id
        for root, dirs, files in os.walk(self.base_dir):
            for file in files:
                if analysis_id[:8] in file:
                    return root
        return None
    
    def list_local_analyses(self) -> List[Dict[str, Any]]:
        """Lista análises salvas localmente"""
        analyses = []
        
        try:
            metadata_dir = os.path.join(self.base_dir, 'metadata')
            
            for file in os.listdir(metadata_dir):
                if file.endswith('_metadata.txt'):
                    file_path = os.path.join(metadata_dir, file)
                    
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                        
                        # Extrai informações básicas do metadata
                        lines = content.split('\n')
                        analysis_info = {}
                        
                        for line in lines:
                            if ':' in line:
                                key, value = line.split(':', 1)
                                analysis_info[key.strip().lower().replace(' ', '_')] = value.strip()
                        
                        analyses.append({
                            'metadata_file': file,
                            'analysis_id': analysis_info.get('id_da_análise', 'N/A'),
                            'timestamp': analysis_info.get('timestamp', 'N/A'),
                            'segmento': analysis_info.get('segmento', 'N/A'),
                            'total_files': analysis_info.get('total_de_arquivos', 'N/A'),
                            'generated_at': analysis_info.get('gerado_em', 'N/A')
                        })
                        
                    except Exception as e:
                        logger.error(f"❌ Erro ao ler metadata {file}: {str(e)}")
                        continue
            
            # Ordena por timestamp (mais recente primeiro)
            analyses.sort(key=lambda x: x['timestamp'], reverse=True)
            
            return analyses
            
        except Exception as e:
            logger.error(f"❌ Erro ao listar análises locais: {str(e)}")
            return []
    
    def delete_local_analysis(self, analysis_id: str) -> bool:
        """Remove análise local por ID"""
        try:
            deleted_files = 0
            
            # Busca e remove todos os arquivos relacionados
            for root, dirs, files in os.walk(self.base_dir):
                for file in files:
                    if analysis_id[:8] in file:
                        file_path = os.path.join(root, file)
                        try:
                            os.remove(file_path)
                            deleted_files += 1
                            logger.info(f"🗑️ Arquivo removido: {file}")
                        except Exception as e:
                            logger.error(f"❌ Erro ao remover {file}: {str(e)}")
            
            if deleted_files > 0:
                logger.info(f"✅ Análise local removida: {deleted_files} arquivos deletados")
                return True
            else:
                logger.warning(f"⚠️ Nenhum arquivo encontrado para análise {analysis_id}")
                return False
                
        except Exception as e:
            logger.error(f"❌ Erro ao deletar análise local: {str(e)}")
            return False

# Instância global
local_file_manager = LocalFileManager()