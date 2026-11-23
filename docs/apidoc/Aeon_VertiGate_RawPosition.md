---
uid: Aeon.VertiGate.RawPosition
---

Read this register at any time. [EnablePositionEvent](xref:Aeon.VertiGate.ControlFlags.EnablePositionEvent) also reports it with each [Position](xref:Aeon.VertiGate.Position) event.

[Position](xref:Aeon.VertiGate.Position) is Encoder minus Home, divided by 48 and clamped to the range 0 to 255. This pair thus shows the travel that the clamp hides, and the step when a calibration records a new home. One count is 25 µm.
