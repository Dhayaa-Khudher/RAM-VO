from pathlib import Path
import json,csv,collections,re
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import argparse
parser=argparse.ArgumentParser(description='Plot supplied seed-level sparsification curves.')
parser.add_argument('--data-dir',type=Path,default=Path(__file__).resolve().parents[1]/'data/results')
parser.add_argument('--out',type=Path,default=Path(__file__).resolve().parents[1]/'generated')
args=parser.parse_args()
root=args.out
root.mkdir(parents=True,exist_ok=True)
groups=json.loads((args.data_dir/'sparsification_seed_curves.json').read_text())
f=np.arange(20)*.05
trap=np.trapezoid if hasattr(np,'trapezoid') else np.trapz
rows=[]
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.spines.top':False,'axes.spines.right':False,'pdf.fonttype':42})
for condition in ['Normal','Combined']:
 fig,ax=plt.subplots(figsize=(6.2,4.2),layout='constrained')
 for cond,head,pairs in groups:
  if cond!=condition:continue
  a=np.array(pairs); u=a[:,0,:];o=a[:,1,:]
  color='#1764ab' if head=='Initial' else '#c45712'
  for kind,arr,ls in [('Uncertainty',u,'-'),('Oracle',o,'--')]:
   for seedcurve in arr: ax.plot(f,seedcurve,color=color,ls=ls,lw=.8,alpha=.32)
   ax.plot(f,arr.mean(axis=0),color=color,ls=ls,lw=2,label=f'{head}: {kind.lower()}')
   ax.fill_between(f,arr.min(axis=0),arr.max(axis=0),color=color,alpha=.1)
  vals=[]
  for seed,(uc,oc) in zip([42,1234,2023],pairs):
   gap=trap(np.array(uc)-np.array(oc),f);oracle=trap(oc,f);relative=gap/oracle
   rows.append([cond,head,seed,gap,oracle,relative]);vals.append(relative)
  print(cond,head,'mean',np.mean(vals),'SD',np.std(vals,ddof=1))
 ax.set(xlabel='Removed-frame fraction',ylabel='Mean retained translation error (m)',xlim=(0,.95),ylim=(0,None),title=condition+' conditions' if condition=='Normal' else 'Combined visual shift')
 ax.grid(alpha=.18);ax.legend(fontsize=8,loc='upper right')
 name='Figure_10_a_sparsification_normal' if condition=='Normal' else 'Figure_10_b_sparsification_combined'
 fig.savefig(root/(name+'.png'),dpi=300);fig.savefig(root/(name+'.pdf'));plt.close(fig)
with (root/'relative_ause_calculations.csv').open('w') as file:
 w=csv.writer(file);w.writerow(['condition','head','seed','gap_integral_m','oracle_integral_m','relative_ause']);w.writerows(rows)
