# Text extracted from the original environment setup notes

three worlds (train / val / generalization)

Nav2-safe costmap checklist tuned for TB4.



TB4’s camera height (~0.3–0.4 m) and LiDAR favor:

Mid-height objects (0.4–1.2 m) → strong VO features

Clear vertical edges → better yaw & lateral motion

Nav2-friendly footprints → stable costmaps



VO does NOT benefit from realistic furniture branding or smooth colors.It benefits from repeatable, spatially rich, high-frequency visual cues.



For CNN / CNN-LSTM / CNN-Transformer VO, textures should provide:

Corners, edges, grain variations

Avoid flat colors

Avoid large periodic tiling

Prevent scale ambiguity

No shiny reflections

No specular highlights

No dynamic lighting baked into texture

Bad for VO

Why

Logos / text (“IKEA”)

Network learns text, not motion

Smooth surfaces

No features to track

Large uniform color

Optical flow collapse

Strong directional patterns

Bias motion estimation

Photo-real shadows baked in

Break photometric consistency



✔ Natural noise✔ Rich gradients✔ Stable under motion

👉 Example: oak, birch, plywood (light or mid tone)



✔ Ideal for learning motion✔ No semantic bias

Use when you want pure geometric VO



✔ High-frequency✔ No strong orientation

Excellent for indoor robots (TB4)



✔ Perfect for planar motion✔ Strong optical flow



Use muted colors, not saturated ones.

Light gray

Beige

Pale blue

Soft green

Off-white

Pure white

Pure black

Neon colors

Strong reds

📌 Your light blue + green direction is correct, but must include texture noise, not flat paint.



Light plaster texture

Subtle grain

Slight color variation (±5%)

Fine concrete or asphalt

Medium contrast

No sharp repeating tiles

Desaturated wood

Remove logos

Different texture per object (important!)



In GIMP:

Select → By Color → Black text

Delete / Fill with texture clone



convert base.png \

-attenuate 0.15 +noise Gaussian \

vo_ready.png



convert vo_ready.png -modulate 100,70,100 vo_final.png



Use

Resolution

Walls

1024×1024

Floors

2048×2048

Objects

512–1024

📌 Bigger is NOT always better — consistency matters more.



I can prepare:

✅ VO_wall_plaster.png

✅ VO_floor_concrete.png

✅ VO_wood_light.png

✅ VO_wood_dark.png

✅ VO_noise_generic.png

All:

Tile-safe

No logos

Optimized contrast

Gazebo-ready

Just tell me:

Indoor or outdoor?Walls only or full world?Resolution preference?

This is exactly the level that will strengthen your VO paper results, not just visuals.


