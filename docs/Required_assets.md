# Resources still needed

The supplied seven SDF files and nine COLLADA meshes are included unchanged. The dependency inventory finds 45 missing local resource paths, including texture references inside the meshes. Add the original files at the following repository paths:

- `simulation/models/LockerBig/meshes/locker.obj`
- `simulation/models/office_cabinet/meshes/WhiteCabinet.obj`
- `simulation/models/office_cafe_table/model.sdf`
- `simulation/models/sofa/meshes/Sofa.obj`
- `simulation/models/textures/Blue.png`
- `simulation/models/textures/FLOOR_Albedo.png`
- `simulation/models/textures/Floor_6.png`
- `simulation/models/textures/Gray.png`
- `simulation/models/textures/Green.png`
- `simulation/models/textures/Red.png`
- `simulation/models/textures/Yellow.png`
- `simulation/models/textures/ceiling_01.png`
- `simulation/models/textures/office_chair_diffuse.png`
- `simulation/models/textures/office_chair_specular.png`
- `simulation/models/textures/office_desk_diffuse.png`
- `simulation/models/textures/pattern_01.png`
- `simulation/models/textures/pattern_02.png`
- `simulation/models/textures/pattern_03.png`
- `simulation/models/textures/plywood256x256.png`
- `simulation/models/textures/poster_01.png`
- `simulation/models/textures/poster_02.png`
- `simulation/models/textures/poster_03.png`
- `simulation/models/textures/poster_04.png`
- `simulation/models/textures/tape_red.png`
- `simulation/models/textures/tape_yellow.png`
- `simulation/models/textures/wall_16.png`
- `simulation/models/textures/wall_17.png`
- `simulation/models/textures/wall_18.png`
- `simulation/models/textures/wall_29.png`
- `simulation/models/textures/wall_30.png`
- `simulation/models/textures/wall_31.png`
- `simulation/models/textures/wall_noise_blue.png`
- `simulation/models/textures/wall_noise_green.png`
- `simulation/models/wall_1.sdf`
- `simulation/models/wall_10.sdf`
- `simulation/models/wall_11.sdf`
- `simulation/models/wall_12.sdf`
- `simulation/models/wall_2.sdf`
- `simulation/models/wall_3.sdf`
- `simulation/models/wall_4.sdf`
- `simulation/models/wall_5.sdf`
- `simulation/models/wall_6.sdf`
- `simulation/models/wall_7.sdf`
- `simulation/models/wall_8.sdf`
- `simulation/models/wall_9.sdf`

The office world contains no robot or camera sensor definition. Robot/camera descriptions, bridge configuration, launch changes, and custom Nav2 settings must be supplied separately. Original collection, perturbation, model-training and evaluation scripts, checkpoints, and route-level records are also not supplied.

The XML and dependency checks do not establish that Gazebo can launch this environment. Third-party mesh and texture redistribution terms must accompany any public release.
