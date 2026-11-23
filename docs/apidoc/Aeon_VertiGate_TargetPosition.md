---
uid: Aeon.VertiGate.TargetPosition
---

A value of 0 lowers the gate fully down, and a value of 255 raises it fully up. Each value between the two moves the gate to the matching position. One count is 1.2 mm.

The gate stops at step 250. A write of 251 to 255 moves the gate to the same position as a write of 250.
