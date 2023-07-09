import os
import importlib.util

# Directory path
dir_path = "./Manual Annotations"

# Initialize counters
total_objects = 0
non_interruption = 0
interruption = 0
concerning_content = 0
concerning_action = 0

# Iterate over files
for filename in os.listdir(dir_path):
    if filename.endswith('.py'):
        spec = importlib.util.spec_from_file_location("module.name", os.path.join(dir_path, filename))
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        total_objects += len(module.data)

        # Iterate over dictionaries in the current file
        for obj in module.data:
            if obj['classification'] == 'non-interruption':
                non_interruption += 1
            elif obj['classification'] == 'interruption':
                interruption += 1
                if obj['sub-classification'] == 'concerning content':
                    concerning_content += 1
                elif obj['sub-classification'] == 'concerning action':
                    concerning_action += 1

# Calculate percentages
non_interruption_pct = (non_interruption / total_objects) * 100
interruption_pct = (interruption / total_objects) * 100
concerning_content_pct = (concerning_content / interruption) * 100 if interruption != 0 else 0
concerning_action_pct = (concerning_action / interruption) * 100 if interruption != 0 else 0

# Print results
print(f'Count: {total_objects}')
print(f'Interruption: {interruption} ({interruption_pct:.1f}%)')
print(f'Non-interruption: {non_interruption} ({non_interruption_pct:.1f}%)')
print(f'Concerning content: {concerning_content} ({concerning_content_pct:.1f}%)')
print(f'Concerning action: {concerning_action} ({concerning_action_pct:.1f}%)')