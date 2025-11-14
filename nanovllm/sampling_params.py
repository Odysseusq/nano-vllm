from dataclasses import dataclass


@dataclass
class SamplingParams:
    mask_token_id: int = 151669
    temperature: float = 1.0
    max_tokens: int = 64
    ignore_eos: bool = False

    def __post_init__(self):
        assert self.temperature > 1e-10, "greedy sampling is not permitted"
