from google.adk.agents import BaseAgent, SequentialAgent
from google.adk.agents.invocation_context import InvocationContext
from google.adk.events import Event
from typing import AsyncGenerator

class LogMaterialReceiptAgent(BaseAgent):
    name: str = "log_material_receipt"
    async def _run_async_impl(self, context: InvocationContext) -> AsyncGenerator[Event, None]:
        context.session.state["stage_log"] = context.session.state.get("stage_log", "Batch opened") + " -> Raw materials received"
        yield Event(author=self.name, content=None)

class LogFormulationCompleteAgent(BaseAgent):
    name: str = "log_formulation_complete"
    async def _run_async_impl(self, context: InvocationContext) -> AsyncGenerator[Event, None]:
        context.session.state["stage_log"] += " -> Formulation complete"
        yield Event(author=self.name, content=None)

class LogQCCheckAgent(BaseAgent):
    name: str = "log_qc_check"
    async def _run_async_impl(self, context: InvocationContext) -> AsyncGenerator[Event, None]:
        context.session.state["stage_log"] += " -> QC checkpoint passed"
        yield Event(author=self.name, content=None)

# ADK's CLI specifically looks for a variable named root_agent
root_agent = SequentialAgent(
    name="batch_tracker_pipeline",
    sub_agents=[LogMaterialReceiptAgent(), LogFormulationCompleteAgent(), LogQCCheckAgent()],
)