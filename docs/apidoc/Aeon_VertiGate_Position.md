---
uid: Aeon.VertiGate.Position
---

The scale is the same as [TargetPosition](xref:Aeon.VertiGate.TargetPosition). One count is 1.2 mm, and the value stops at 250.

Read this register at any time. [EnablePositionEvent](xref:Aeon.VertiGate.ControlFlags.EnablePositionEvent) also reports it while the gate moves or homes.

Homing measures against the old home until the device records the new one. The value thus steps at the end of a calibration.
