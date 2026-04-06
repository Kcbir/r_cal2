import json
with open('/Users/kabir/Desktop/CAL/FinReflectKG_Complete_Pipeline.ipynb', 'r') as f:
    nb = json.load(f)

print('Notebook cell summary:')
print('=' * 60)
for i, cell in enumerate(nb['cells'][:15]):
    src = ''.join(cell['source'])
    first_line = src.split('\n')[0][:50]
    print(f'{i+1:2}. [{cell["cell_type"][:4]}] {first_line}...')

print()
print('Checking for problematic references...')
full_src = ' '.join(''.join(c['source']) for c in nb['cells'])

if 'anim3013/finreflectkg-multihopqa' in full_src:
    print('  WARNING: Still references anim3013/finreflectkg-multihopqa')
else:
    print('  OK: No reference to wrong dataset')

if 'domyn/FinReflectKG' in full_src:
    print('  OK: Uses domyn/FinReflectKG')
else:
    print('  WARNING: Missing domyn/FinReflectKG reference')

if 'train_file' in full_src:
    print(f'  WARNING: Still has references to train_file (old format)')
else:
    print('  OK: No train_file references')
