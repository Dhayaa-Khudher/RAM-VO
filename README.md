# RAM-VO research resources

Supporting files for **Reliability-Aware Temporal Memory for Drift Reduction in End-to-End Planar Visual Odometry under Visual Domain Shift**, by Dhayaa R. Khudher and Roger Powell.

## Contents of this release preparation

- An original office-world SDF, four furniture zones, cubicle and tile model SDFs, and nine COLLADA meshes.
- Original environment and data-collection notes, retained without rewriting their experimental commands.
- Selected environment screenshots.
- Available trajectory-averaged uncertainty curves, seed-level ablation values, selected validation outcomes, and aggregate memory-event/extended-path measurements.
- The plotting script used for the available sparsification curves.

This package is an initial resource collection. It does not yet contain all dependencies required to render the world or regenerate the complete experiment. See `docs/Required_assets.md` and `docs/model_dependencies.csv` for the model and texture references still needed.

## Environment recorded in the supplied notes

Ubuntu 24.04, ROS 2 Jazzy, and Gazebo Harmonic 8.9.0. The notes launch the robot through `nav2_bringup/tb4_simulation_launch.py`. The uploaded world itself contains no robot or camera definition. The camera calibration reported in the paper must therefore be linked to the original spawned-robot configuration before claiming complete regeneration.

The historical collection/training notes contain pilot commands using 30 epochs, learning rate 3e-4, and 192 x 256 inputs. They are not the final paper's 100-epoch, 1e-4, 256 x 256 training protocol. Do not use the pilot commands as a reproduction recipe for the reported model.

## Repository layout

| Directory | Contents |
|---|---|
| `simulation/worlds/` | Original office world |
| `simulation/models/` | Furniture zones, cubicle/tile models, and supplied meshes |
| `docs/original_notes/` | Unmodified uploaded notes and an extracted ODT text copy |
| `data/results/` | Available numerical summaries and uncertainty arrays |
| `evaluation/` | Sparsification plotting script |
| `media/environment/` | Selected uploaded environment views |

## Dependency inventory

From this repository root, run:

```bash
python3 evaluation/check_sdf_resources.py
```

This checks XML parsing and inventories active SDF resource references and COLLADA image paths. Relative image paths are interpreted relative to their mesh; `model://` paths are checked beneath `simulation/models/`. It does not validate SDF semantics, resolve globally installed/Fuel resources, or start Gazebo. Missing local resources cause a nonzero exit code. All seven SDF files and nine COLLADA meshes were XML-parsed during packaging; simulation launch has not been tested here.

## Available numerical records

`data/results/sparsification_curves.csv` contains the trajectory-averaged uncertainty and oracle curves per seed, condition, and output head. Relative AUSE uses the ratio of integrated mean curves over removal fractions 0 to 0.95. `relative_ause_calculations.csv` includes the two trapezoidal integrals and their ratio.

`ablation_per_seed.csv` retains supplied per-seed ATE and sample standard deviations. `selected_validation.csv` describes the selected configuration only. `memory_count_summary.csv` and `extended_path_summary.csv` contain aggregate measurements, not individual event logs or spatial trajectories. The JSON files preserve the supporting arrays.

For the sparsification plots, install NumPy and Matplotlib, run from the repository root:

```bash
python3 evaluation/build_sparsification.py
```

The plotted files and recomputed relative-AUSE CSV are written to `generated/`. The original supplied data remain unchanged. No VO model is retrained or evaluated by that script.

## Resources to add for full experimental reproduction

1. Referenced meshes, textures, furniture models, and wall SDFs.
2. Robot/camera descriptions, ROS-Gazebo bridge settings, launch files, and Nav2 configuration.
3. Original perturbation-generation and data-extraction scripts.
4. Route definitions, trajectory-disjoint split manifest, recorded ground truth, estimates, and event logs.
5. Final model implementations, training/evaluation scripts, and checkpoint availability instructions.

The original notes refer to `extract_vo_dataset.py`, `train_vo_baseline.py`, `train_vo_cnn_lstm.py`, `eval_vo_metrics.py`, and `eval_vo_metrics_cnn_lstm.py`; these script bodies have not been supplied in this package.

## Media and licensing

Videos remain in the separately supplied environment-media archive and can be attached to a repository release. The React project is separate from the simulation collection and is not included here. A license should be chosen by the authors after confirming redistribution terms for third-party meshes and textures. No third-party license is assigned by this package.

## Contact

Dhayaa R. Khudher, University of Basrah: dhayaa.khudher@uobasrah.edu.iq
