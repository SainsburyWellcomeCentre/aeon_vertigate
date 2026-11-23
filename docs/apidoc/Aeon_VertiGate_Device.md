---
uid: Aeon.VertiGate.Device
---

Use the [Harp device pattern](https://harp-tech.org/articles/operators.html#device-pattern) to initialize the device, log data, and send commands to and receive messages from the VertiGate.

:::workflow
![Harp Device Pattern](../workflows/harp-devicepattern.bonsai)
:::

Check out the following in-depth guides to learn how to access the device functionality with the `Aeon.VertiGate` package:
- [Calibrate the Gate](../articles/calibrate-the-gate.md)
- [Tune Speed and Torque](../articles/tune-the-motion.md)
- [Move the Gate](../articles/move-the-gate.md)
- [Monitor the Servo](../articles/monitor-the-servo.md)

Refer to the register table below for a complete listing of the available registers on the device.

<table>
  <thead>
    <tr><th colspan="2">VertiGate</th></tr>
  </thead>
  <tbody>
    <tr><td>whoAmI</td><td>3002</td></tr>
    <tr><td>firmwareVersion</td><td>0.1</td></tr>
    <tr><td>hardwareTargets</td><td>0.1</td></tr>
  </tbody>
</table>

### Registers

| name | address | type | length | access | description | range | interfaceType |
|-|-|-|-|-|-|-|-|
| [Control](xref:Aeon.VertiGate.Control) | 32 | U8 |  | Write | Sends a command to the gate and reports the active states. |  | [ControlFlags](xref:Aeon.VertiGate.ControlFlags) |
| [TargetPosition](xref:Aeon.VertiGate.TargetPosition) | 33 | U8 |  | Write | Sets the target position of the gate. | [0:255] | |
| [GateState](xref:Aeon.VertiGate.GateState) | 34 | U8 |  | Event | Reports the current state of the gate. |  | [GateStatus](xref:Aeon.VertiGate.GateStatus) |
| [Speed](xref:Aeon.VertiGate.Speed) | 35 | U8 |  | Write | Sets the movement speed of the gate. | 255 [0:255] | |
| [Torque](xref:Aeon.VertiGate.Torque) | 36 | U8 |  | Write | Sets the torque limit of the gate motor. | 35 [0:127] | |
| [CalibrationOffset](xref:Aeon.VertiGate.CalibrationOffset) | 37 | S8 |  | Write | Sets the offset applied to the fully-raised position of the gate. | 0 [-128:127] | |
| [MotorState](xref:Aeon.VertiGate.MotorState) | 38 | U8 |  | Event | Reports whether the motor holds the gate. |  | [MotorStatus](xref:Aeon.VertiGate.MotorStatus) |
| [Position](xref:Aeon.VertiGate.Position) | 39 | U8 |  | Event | Reports the current position of the gate. | [0:255] | |
| [ServoTelemetry](xref:Aeon.VertiGate.ServoTelemetry) | 40 | S16 | 4 | Event | Reports the voltage, temperature, current and error status of the servo. |  | [ServoTelemetryPayload](xref:Aeon.VertiGate.ServoTelemetryPayload) |
| [RawPosition](xref:Aeon.VertiGate.RawPosition) | 41 | S32 | 2 | Event | Reports the encoder counts used to calculate the gate position. |  | [RawPositionPayload](xref:Aeon.VertiGate.RawPositionPayload) |
