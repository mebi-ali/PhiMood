import torch
from transformers import AutoModelForCausalLM, AutoTokenizer





class Model:
    def __init__(self) -> None:
        torch.set_default_device("cpu")
        model_name = "microsoft/phi-2"
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch.float32,
            device_map="auto",
            trust_remote_code=True,
        )
        self.tokenizer = AutoTokenizer.from_pretrained(
            model_name, trust_remote_code=True
        )

    def process(self, prompt):

        inputs = self.tokenizer(
            f"""Instruct: Create a funny joke on the given phrase  '{prompt}'.
                                 Output: 
                                 """,
            return_tensors="pt",
            return_attention_mask=True,
        )
        inputs = inputs.to("cpu")

        outputs = self.model.generate(
            **inputs, max_length=200
        )
        return self.tokenizer.batch_decode((outputs)[0])


# if __name__ == "__main__":
#     model = Model()
#     print(model.process("a cup of coffee"))
