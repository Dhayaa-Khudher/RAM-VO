"""Inventory local SDF and COLLADA references; not a simulator launch test."""
from pathlib import Path
import xml.etree.ElementTree as ET
import sys
import csv

root = Path(__file__).resolve().parents[1]
models = root / "simulation/models"
records = []
files = sorted((root / "simulation").rglob("*.sdf")) + sorted(models.rglob("*.dae"))
for path in files:
    document = ET.parse(path)
    references = []
    if path.suffix == ".sdf":
        for node in document.iter():
            value = (node.text or "").strip()
            if value.startswith(("model://", "file://")):
                references.append((node.tag, value))
    else:
        for node in document.iter():
            if node.tag.split("}")[-1] == "library_images":
                for image_node in node.iter():
                    if image_node.tag.split("}")[-1] == "init_from":
                        value = (image_node.text or "").strip()
                        if value:
                            references.append(("COLLADA image", value))
    for element, value in references:
        if value.startswith("model://"):
            target = models / value[len("model://"):]
        elif value.startswith("file://"):
            target = Path(value[len("file://"):])
        else:
            target = path.parent / value
        target = target.resolve()
        inside = target.is_relative_to(root)
        present = inside and target.is_file()
        shown = target.relative_to(root).as_posix() if inside else str(target)
        records.append({"source":path.relative_to(root).as_posix(),"element":element,"uri":value,"repository_target":shown,"present":present})
with (root / "docs/model_dependencies.csv").open("w", newline="") as stream:
    writer = csv.DictWriter(stream,fieldnames=["source","element","uri","repository_target","present"])
    writer.writeheader()
    writer.writerows(records)
missing = sorted({r["repository_target"] for r in records if not r["present"]})
print(f"XML parsed: {len(files)} SDF/COLLADA files")
for target in missing:
    print("Missing repository resource:", target)
print(f"Missing unique resources: {len(missing)}")
sys.exit(1 if missing else 0)
