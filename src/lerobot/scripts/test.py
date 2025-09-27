from lerobot.policies import get_policy_class
from lerobot.processor import PolicyProcessorPipeline

# The preprocessor and postprocessor are now external
preprocessor = PolicyProcessorPipeline.from_pretrained("lerobot/smolvla_base", config_filename="preprocessor_config.json")
postprocessor = PolicyProcessorPipeline.from_pretrained("lerobot/smolvla_base", config_filename="postprocessor_config.json")
policy = get_policy_class("your-policy-type").from_pretrained("lerobot/smolvla_base")

# Process data through the pipeline
# processed_batch = preprocessor(raw_batch)
# action = policy(processed_batch)
# final_action = postprocessor(action)