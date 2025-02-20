"""
Code for Agents.
"""
from .agent import Agent, AgentOptions, AgentCallbacks, AgentProcessingResult, AgentResponse


try:
    from .lambda_agent import LambdaAgent, LambdaAgentOptions
    from .bedrock_llm_agent import BedrockLLMAgent, BedrockLLMAgentOptions
    from .lex_bot_agent import LexBotAgent, LexBotAgentOptions
    from .amazon_bedrock_agent import AmazonBedrockAgent, AmazonBedrockAgentOptions
    from .comprehend_filter_agent import ComprehendFilterAgent, ComprehendFilterAgentOptions
    from .bedrock_translator_agent import BedrockTranslatorAgent, BedrockTranslatorAgentOptions
    from .chain_agent import ChainAgent, ChainAgentOptions
    from .bedrock_inline_agent import BedrockInlineAgent, BedrockInlineAgentOptions
    from .bedrock_flows_agent import BedrockFlowsAgent, BedrockFlowsAgentOptions
    _AWS_AVAILABLE = True
except ImportError:
    _AWS_AVAILABLE = False
try:
    from .anthropic_agent import AnthropicAgent, AnthropicAgentOptions
    _ANTHROPIC_AVAILABLE = True
except ImportError:
    _ANTHROPIC_AVAILABLE = False


try:
    from .openai_agent import OpenAIAgent, OpenAIAgentOptions
    _OPENAI_AVAILABLE = True
except ImportError:
    _OPENAI_AVAILABLE = False

try:
    from .deepseek_agent import DeepSeekAgent, DeepSeekAgentOptions
    _DEEPSEEK_AVAILABLE = True
except ImportError:
    _DEEPSEEK_AVAILABLE = False

from .supervisor_agent import SupervisorAgent, SupervisorAgentOptions


__all__ = [
    'Agent',
    'AgentOptions',
    'AgentCallbacks',
    'AgentProcessingResult',
    'AgentResponse',
    'SupervisorAgent',
    'SupervisorAgentOptions'
    ]


if _AWS_AVAILABLE :
    __all__.extend([
        'LambdaAgent',
        'LambdaAgentOptions',
        'BedrockLLMAgent',
        'BedrockLLMAgentOptions',
        'LexBotAgent',
        'LexBotAgentOptions',
        'AmazonBedrockAgent',
        'AmazonBedrockAgentOptions',
        'ComprehendFilterAgent',
        'ComprehendFilterAgentOptions',
        'ChainAgent',
        'ChainAgentOptions',
        'BedrockTranslatorAgent',
        'BedrockTranslatorAgentOptions',
        'BedrockInlineAgent',
        'BedrockInlineAgentOptions',
        'BedrockFlowsAgent',
        'BedrockFlowsAgentOptions'
    ])


if _ANTHROPIC_AVAILABLE:
    __all__.extend([
        'AnthropicAgent',
        'AnthropicAgentOptions'
    ])


if _OPENAI_AVAILABLE:
    __all__.extend([
            'OpenAIAgent',
            'OpenAIAgentOptions'
        ])
