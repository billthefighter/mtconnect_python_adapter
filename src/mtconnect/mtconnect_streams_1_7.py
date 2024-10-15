from dataclasses import dataclass, field
from enum import Enum
from typing import Any, List, Optional, Union

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "urn:mtconnect.org:MTConnectStreams:1.7"


class ActuatorStateValueType(Enum):
    """
    Controlled vocabulary for ActuatorState.

    :cvar ACTIVE: The value of the {{term(Data Entity)}} that is
        engaging.
    :cvar INACTIVE: The value of the {{term(Data Entity)}} that is not
        engaging.
    :cvar UNAVAILABLE: Value is indeterminate
    """

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    UNAVAILABLE = "UNAVAILABLE"


class AlarmStateType(Enum):
    """DEPRECATED: The active or cleared state of the notification

    :cvar ACTIVE: The notification is active
    :cvar CLEARED: The notification has been cleared
    """

    ACTIVE = "ACTIVE"
    CLEARED = "CLEARED"


class AvailabilityValueType(Enum):
    """
    Controlled vocabulary for Availability.

    :cvar AVAILABLE: The value or status of an XML element when it is
        available.
    :cvar UNAVAILABLE: The value of the {{term(Data Entity)}} either
        when the data is not received or the entity is incapable of
        providing data.
    """

    AVAILABLE = "AVAILABLE"
    UNAVAILABLE = "UNAVAILABLE"


class AxisCouplingValueType(Enum):
    """
    Controlled vocabulary for AxisCoupling.

    :cvar TANDEM: Elements are physically connected to each other and
        operate as a single unit.
    :cvar SYNCHRONOUS: Physical or logical parts which are not
        physically connected to each other but are operating together.
    :cvar MASTER: It provides information or state values that
        influences the operation of other {{block(DataItem)}} of similar
        type.
    :cvar SLAVE: The axis is a slave to the {{block(COUPLED_AXES)}}
    :cvar UNAVAILABLE: Value is indeterminate
    """

    TANDEM = "TANDEM"
    SYNCHRONOUS = "SYNCHRONOUS"
    MASTER = "MASTER"
    SLAVE = "SLAVE"
    UNAVAILABLE = "UNAVAILABLE"


class AxisInterlockValueType(Enum):
    """
    Controlled vocabulary for AxisInterlock.

    :cvar ACTIVE: The value of the {{term(Data Entity)}} that is
        engaging.
    :cvar INACTIVE: The value of the {{term(Data Entity)}} that is not
        engaging.
    :cvar UNAVAILABLE: Value is indeterminate
    """

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    UNAVAILABLE = "UNAVAILABLE"


class AxisStateValueType(Enum):
    """
    Controlled vocabulary for AxisState.

    :cvar HOME: The component at its home position.
    :cvar TRAVEL: The component is in motion.
    :cvar PARKED: The component has been moved to a fixed position.
    :cvar STOPPED: The component is stopped.
    :cvar UNAVAILABLE: Value is indeterminate
    """

    HOME = "HOME"
    TRAVEL = "TRAVEL"
    PARKED = "PARKED"
    STOPPED = "STOPPED"
    UNAVAILABLE = "UNAVAILABLE"


class ChuckInterlockValueType(Enum):
    """
    Controlled vocabulary for ChuckInterlock.

    :cvar ACTIVE: The value of the {{term(Data Entity)}} that is
        engaging.
    :cvar INACTIVE: The value of the {{term(Data Entity)}} that is not
        engaging.
    :cvar UNAVAILABLE: Value is indeterminate
    """

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    UNAVAILABLE = "UNAVAILABLE"


class ChuckStateValueType(Enum):
    """
    Controlled vocabulary for ChuckState.

    :cvar OPEN: A component is open to the point of a positive
        confirmation.
    :cvar CLOSED: A component is closed to the point of a positive
        confirmation.
    :cvar UNLATCHED: An intermediate position.
    :cvar UNAVAILABLE: Value is indeterminate
    """

    OPEN = "OPEN"
    CLOSED = "CLOSED"
    UNLATCHED = "UNLATCHED"
    UNAVAILABLE = "UNAVAILABLE"


class ConnectionStatusValueType(Enum):
    """
    Controlled vocabulary for ConnectionStatus.

    :cvar CLOSED: represents no connection at all.
    :cvar LISTEN: represents the {{term(Agent)}} waiting for a
        connection request from an {{term(Adapter)}}.
    :cvar ESTABLISHED: represents an open connection. The normal state
        for the data transfer phase of the connection.
    :cvar UNAVAILABLE: Value is indeterminate
    """

    CLOSED = "CLOSED"
    LISTEN = "LISTEN"
    ESTABLISHED = "ESTABLISHED"
    UNAVAILABLE = "UNAVAILABLE"


class ControllerModeOverrideValueType(Enum):
    """
    Controlled vocabulary for ControllerModeOverride.

    :cvar ON: On state or value.
    :cvar OFF: Off state or value.
    :cvar UNAVAILABLE: Value is indeterminate
    """

    ON = "ON"
    OFF = "OFF"
    UNAVAILABLE = "UNAVAILABLE"


class ControllerModeValueType(Enum):
    """
    Controlled vocabulary for ControllerMode.

    :cvar AUTOMATIC: The {{block(Controller)}} is configured to
        automatically execute a program.
    :cvar MANUAL: Operations based on the instructions received from an
        external source.
    :cvar MANUAL_DATA_INPUT: The operator can enter a series of
        operations for the controller to perform.
    :cvar SEMI_AUTOMATIC: The controller executes a single set of
        instructions from an active program and then stops until given a
        command to execute the next set of instructions.
    :cvar EDIT: The controller is currently functioning as a programming
        device and is not capable of executing an active program.
    :cvar UNAVAILABLE: Value is indeterminate
    """

    AUTOMATIC = "AUTOMATIC"
    MANUAL = "MANUAL"
    MANUAL_DATA_INPUT = "MANUAL_DATA_INPUT"
    SEMI_AUTOMATIC = "SEMI_AUTOMATIC"
    EDIT = "EDIT"
    UNAVAILABLE = "UNAVAILABLE"


class DataItemEnumEnum(Enum):
    """
    The types of measurements available.

    :cvar ACCELERATION: The measurement of the rate of change of
        velocity.
    :cvar ACCUMULATED_TIME: The measurement of accumulated time for an
        activity or event.
    :cvar AMPERAGE: **DEPRECATED** in *Version 1.6*. Replaced by
        `AMPERAGE_AC` and `AMPERAGE_DC`. The measurement of electrical
        current.
    :cvar ANGLE: The measurement of angular position.
    :cvar ANGULAR_ACCELERATION: The measurement rate of change of
        angular velocity.
    :cvar ANGULAR_VELOCITY: The measurement of the rate of change of
        angular position.
    :cvar AXIS_FEEDRATE: The measurement of the feedrate of a linear
        axis.
    :cvar CAPACITY_FLUID: The fluid capacity of an object or container.
    :cvar CAPACITY_SPATIAL: The geometric capacity of an object or
        container.
    :cvar CLOCK_TIME: The value provided by a timing device at a
        specific point in time.
    :cvar CONCENTRATION: The measurement of the percentage of one
        component within a mixture of components
    :cvar CONDUCTIVITY: The measurement of the ability of a material to
        conduct electricity.
    :cvar CUTTING_SPEED: The speed difference (relative velocity)
        between the cutting mechanism and the surface of the workpiece
        it is operating on.
    :cvar DENSITY: The volumetric mass of a material per unit volume of
        that material.
    :cvar DEPOSITION_ACCELERATION_VOLUMETRIC: The rate of change in
        spatial volume of material deposited in an additive
        manufacturing process.
    :cvar DEPOSITION_DENSITY: The density of the material deposited in
        an additive manufacturing process per unit of volume.
    :cvar DEPOSITION_MASS: The mass of the material deposited in an
        additive manufacturing process.
    :cvar DEPOSITION_RATE_VOLUMETRIC: The rate at which a spatial volume
        of material is deposited in an additive manufacturing process.
    :cvar DEPOSITION_VOLUME: The spatial volume of material to be
        deposited in an additive manufacturing process.
    :cvar DISPLACEMENT: The measurement of the change in position of an
        object.
    :cvar ELECTRICAL_ENERGY: The measurement of electrical energy
        consumption by a component.
    :cvar EQUIPMENT_TIMER: The measurement of the amount of time a piece
        of equipment or a sub-part of a piece of equipment has performed
        specific activities.
    :cvar FILL_LEVEL: The measurement of the amount of a substance
        remaining compared to the planned maximum amount of that
        substance.
    :cvar FLOW: The measurement of the rate of flow of a fluid.
    :cvar FREQUENCY: The measurement of the number of occurrences of a
        repeating event per unit time.
    :cvar GLOBAL_POSITION: **DEPRECATED** in Version 1.1
    :cvar LENGTH: The measurement of the length of an object.
    :cvar LEVEL: **DEPRECATED** in *Version 1.2*. See `FILL_LEVEL`.
        Represents the level of a resource.
    :cvar LINEAR_FORCE: A {{term(Force)}} applied to a mass in one
        direction only.
    :cvar LOAD: The measurement of the actual versus the standard rating
        of a piece of equipment.
    :cvar MASS: The measurement of the mass of an object(s) or an amount
        of material.
    :cvar PATH_FEEDRATE: The measurement of the feedrate for the axes,
        or a single axis, associated with a {{block(Path)}} component-a
        vector.
    :cvar PATH_FEEDRATE_PER_REVOLUTION: The feedrate for the axes, or a
        single axis.
    :cvar PATH_POSITION: A measured or calculated position of a control
        point associated with a {{block(Controller)}} element, or
        {{block(Path)}} element if provided, of a piece of equipment.
    :cvar PH: A measure of the acidity or alkalinity of a solution.
    :cvar POSITION: A measured or calculated position of a
        {{block(Component)}} element as reported by a piece of
        equipment.
    :cvar POWER_FACTOR: The measurement of the ratio of real power
        flowing to a load to the apparent power in that AC circuit.
    :cvar PRESSURE: The force per unit area measured relative to
        atmospheric pressure. Commonly referred to as gauge pressure.
    :cvar PROCESS_TIMER: The measurement of the amount of time a piece
        of equipment has performed different types of activities
        associated with the process being performed at that piece of
        equipment.
    :cvar RESISTANCE: The measurement of the degree to which a substance
        opposes the passage of an electric current.
    :cvar ROTARY_VELOCITY: The measurement of the rotational speed of a
        rotary axis.
    :cvar SOUND_LEVEL: The measurement of a sound level or sound
        pressure level relative to atmospheric pressure.
    :cvar SPINDLE_SPEED: **DEPRECATED** in *Version 1.2*. Replaced by
        `ROTARY_VELOCITY`. The rotational speed of the rotary axis.
    :cvar STRAIN: The measurement of the amount of deformation per unit
        length of an object when a load is applied.
    :cvar TEMPERATURE: The measurement of temperature.
    :cvar TENSION: The measurement of a force that stretches or
        elongates an object.
    :cvar TILT: The measurement of angular displacement.
    :cvar TORQUE: The measurement of the turning force exerted on an
        object or by an object.
    :cvar VELOCITY: The measurement of the rate of change of position of
        a {{block(Component)}}.
    :cvar VISCOSITY: The measurement of a fluids resistance to flow.
    :cvar VOLTAGE: **DEPRECATED** in *Version 1.6*. Replaced by
        `VOLTAGE_AC` and `VOLTAGE_DC`. The measurement of electrical
        potential between two points.
    :cvar VOLT_AMPERE: The measurement of the apparent power in an
        electrical circuit, equal to the product of root-mean-square
        (RMS) voltage and RMS current (commonly referred to as VA).
    :cvar VOLT_AMPERE_REACTIVE: The measurement of reactive power in an
        AC electrical circuit (commonly referred to as VAR).
    :cvar VOLUME_FLUID: The fluid volume of an object or container.
    :cvar VOLUME_SPATIAL: The geometric volume of an object or
        container.
    :cvar WATTAGE: The measurement of power flowing through or
        dissipated by an electrical circuit or piece of equipment.
    :cvar AMPERAGE_AC: The measurement of an electrical current that
        reverses direction at regular short intervals.
    :cvar AMPERAGE_DC: The measurement of an electric current flowing in
        one direction only.
    :cvar VOLTAGE_AC: The measurement of the electrical potential
        between two points in an electrical circuit in which the current
        periodically reverses direction.
    :cvar VOLTAGE_DC: The measurement of the electrical potential
        between two points in an electrical circuit in which the current
        is unidirectional.
    :cvar X_DIMENSION: Measured dimension of an entity relative to the X
        direction of the referenced coordinate system.
    :cvar Y_DIMENSION: Measured dimension of an entity relative to the Y
        direction of the referenced coordinate system.
    :cvar Z_DIMENSION: Measured dimension of an entity relative to the Z
        direction of the referenced coordinate system.
    :cvar DIAMETER: The measured dimension of a diameter.
    :cvar ORIENTATION: A measured or calculated orientation of a plane
        or vector relative to a cartesian coordinate system.
    :cvar HUMIDITY_RELATIVE: The amount of water vapor present expressed
        as a percent to reach saturation at the same temperature.
    :cvar HUMIDITY_ABSOLUTE: The amount of water vapor expressed in
        grams per cubic meter.
    :cvar HUMIDITY_SPECIFIC: The ratio of the water vapor present over
        the total weight of the water vapor and air present expressed as
        a percent.
    :cvar OBSERVATION_UPDATE_RATE: The average rate of change of values
        for data items in the MTConnect streams. The average is computed
        over a rolling window defined by the implementation.
    :cvar ASSET_UPDATE_RATE: The average rate of change of values for
        assets in the MTConnect streams. The average is computed over a
        rolling window defined by the implementation.
    :cvar PRESSURIZATION_RATE: The change of pressure per unit time.
    :cvar DECELERATION: Negative rate of change of velocity.
    :cvar ANGULAR_DECELERATION: Negative rate of change of angular
        velocity.
    :cvar PRESSURE_ABSOLUTE: The force per unit area measured relative
        to a vacuum.
    :cvar ACTIVE_AXES: The set of axes currently associated with a
        {{block(Path)}} or {{block(Controller)}} {{term(Structural
        Element)}}.
    :cvar ACTUATOR_STATE: Represents the operational state of an
        apparatus for moving or controlling a mechanism or system.
    :cvar ALARM: **DEPRECATED:** Replaced with {{block(CONDITION)}}
        category data items in Version 1.1.0.
    :cvar ASSET_CHANGED: The {{block(assetId)}} of the asset that has
        been added or changed.
    :cvar ASSET_REMOVED: The {{block(assetId)}} of the asset that has
        been removed.
    :cvar AVAILABILITY: Represents the {{term(Agent)}}'s ability to
        communicate with the data source.
    :cvar AXIS_COUPLING: Describes the way the axes will be associated
        to each other. This is used in conjunction with
        {{block(COUPLED_AXES)}} to indicate the way they are
        interacting.
    :cvar AXIS_FEEDRATE_OVERRIDE: The value of a signal or calculation
        issued to adjust the feedrate of an individual linear type axis.
    :cvar AXIS_INTERLOCK: An indicator of the state of the axis lockout
        function when power has been removed and the axis is allowed to
        move freely.
    :cvar AXIS_STATE: An indicator of the controlled state of a
        {{block(Linear)}} or {{block(Rotary)}} component representing an
        axis.
    :cvar BLOCK: The line of code or command being executed by a
        {{block(Controller)}} {{term(Structural Element)}}.
    :cvar BLOCK_COUNT: The total count of the number of blocks of
        program code that have been executed since execution started.
    :cvar CHUCK_INTERLOCK: An indication of the operational condition of
        the interlock function for an electronically controller chuck.
    :cvar CHUCK_STATE: An indication of the operating state of a
        mechanism that holds a part or stock material during a
        manufacturing process. It may also represent a mechanism that
        holds any other mechanism in place within a piece of equipment.
    :cvar CLOSE_CHUCK: Service to close a chuck.
    :cvar CLOSE_DOOR: Service to close a door.
    :cvar CODE: **DEPRECATED** in *Version 1.1*. The programmatic code
        being executed.
    :cvar COMPOSITION_STATE: An indication of the operating condition of
        a mechanism represented by a {{block(Composition)}} type
        element.
    :cvar CONTROLLER_MODE: The current operating mode of the
        {{block(Controller)}} component.
    :cvar CONTROLLER_MODE_OVERRIDE: A setting or operator selection that
        changes the behavior of a piece of equipment.
    :cvar COUPLED_AXES: Refers to the set of associated axes.
    :cvar DATE_CODE: The time and date code associated with a material
        or other physical item.
    :cvar DEVICE_UUID: The identifier of another piece of equipment that
        is temporarily associated with a component of this piece of
        equipment to perform a particular function.
    :cvar DIRECTION: An indication of a fault associated with the
        direction of motion of a {{term(Structural Element)}}.
    :cvar DOOR_STATE: The operational state of a {{block(Door)}}
        component or composition element.
    :cvar EMERGENCY_STOP: The current state of the emergency stop signal
        for a piece of equipment, controller path, or any other
        component or subsystem of a piece of equipment.
    :cvar END_OF_BAR: An indication that the end of a piece of bar stock
        has been reached.
    :cvar EQUIPMENT_MODE: An indication that a piece of equipment, or a
        sub-part of a piece of equipment, is performing specific types
        of activities.
    :cvar EXECUTION: The execution status of the {{block(Component)}}.
    :cvar FUNCTIONAL_MODE: The current intended production status of the
        device or component.
    :cvar HARDNESS: The measurement of the hardness of a material.
    :cvar INTERFACE_STATE: An indication of the operation condition of
        an {{block(Interface)}} component.
    :cvar LINE: **DEPRECATED** in *Version 1.4.0*. The current line of
        code being executed.
    :cvar LINE_LABEL: An optional identifier for a {{block(Block)}} of
        code in a {{block(Program)}}.
    :cvar LINE_NUMBER: A reference to the position of a block of program
        code within a control program.
    :cvar MATERIAL: The identifier of a material used or consumed in the
        manufacturing process.
    :cvar MATERIAL_CHANGE: Service to change the type of material or
        product being loaded or fed to a piece of equipment.
    :cvar MATERIAL_FEED: Service to advance material or feed product to
        a piece of equipment from a continuous or bulk source.
    :cvar MATERIAL_LAYER: Identifies the layers of material applied to a
        part or product as part of an additive manufacturing process.
    :cvar MATERIAL_LOAD: Service to load a piece of material or product.
    :cvar MATERIAL_RETRACT: Service to remove or retract material or
        product.
    :cvar MATERIAL_UNLOAD: Service to unload a piece of material or
        product.
    :cvar MESSAGE: Any text string of information to be transferred from
        a piece of equipment to a client software application.
    :cvar OPEN_CHUCK: Service to open a chuck.
    :cvar OPEN_DOOR: Service to open a door.
    :cvar OPERATOR_ID: The identifier of the person currently
        responsible for operating the piece of equipment.
    :cvar PALLET_ID: The identifier for a pallet.
    :cvar PART_CHANGE: Service to change the part or product associated
        with a piece of equipment to a different part or product.
    :cvar PART_COUNT: The aggregate count of parts.
    :cvar PART_DETECT: An indication designating whether a part or work
        piece has been detected or is present.
    :cvar PART_ID: An identifier of a part in a manufacturing operation.
    :cvar PART_NUMBER: **DEPRECATED** in *Version 1.7*. `PART_NUMBER` is
        now a `subType` of `PART_KIND_ID`. An identifier of a part or
        product moving through the manufacturing process.
    :cvar PATH_FEEDRATE_OVERRIDE: The value of a signal or calculation
        issued to adjust the feedrate for the axes associated with a
        {{block(Path)}} component that may represent a single axis or
        the coordinated movement of multiple axes.
    :cvar PATH_MODE: Describes the operational relationship between a
        {{block(Path)}} {{term(Structural Element)}} and another
        {{block(Path)}} {{term(Structural Element)}} for pieces of
        equipment comprised of multiple logical groupings of controlled
        axes or other logical operations.
    :cvar POWER_STATE: The indication of the status of the source of
        energy for a {{term(Structural Element)}} to allow it to perform
        its intended function or the state of an enabling signal
        providing permission for the {{term(Structural Element)}} to
        perform its functions.
    :cvar POWER_STATUS: **DEPRECATED** in *Version 1.1.0*. The `ON` or
        `OFF` status of the component.
    :cvar PROCESS_TIME: The time and date associated with an activity or
        event.
    :cvar PROGRAM: The name of the logic or motion program being
        executed by the {{block(Controller)}} component.
    :cvar PROGRAM_COMMENT: A comment or non-executable statement in the
        control program.
    :cvar PROGRAM_EDIT: An indication of the status of the
        {{block(Controller)}} components program editing mode. A program
        may be edited while another is executed.
    :cvar PROGRAM_EDIT_NAME: The name of the program being edited. This
        is used in conjunction with {{block(ProgramEdit)}} when in
        `ACTIVE` state.
    :cvar PROGRAM_HEADER: The non-executable header section of the
        control program.
    :cvar PROGRAM_LOCATION: The Uniform Resource Identifier (URI) for
        the source file associated with {{block(Program)}}.
    :cvar PROGRAM_LOCATION_TYPE: Defines whether the logic or motion
        program defined by {{block(Program)}} is being executed from the
        local memory of the controller or from an outside source.
    :cvar PROGRAM_NEST_LEVEL: An indication of the nesting level within
        a control program that is associated with the code or
        instructions that is currently being executed.
    :cvar ROTARY_MODE: The current operating mode for a
        {{block(Rotary)}} type axis.
    :cvar ROTARY_VELOCITY_OVERRIDE: The percentage change to the
        velocity of the programmed velocity for a {{block(Rotary)}} type
        axis.
    :cvar SERIAL_NUMBER: The serial number associated with a
        {{block(Component)}}, {{block(Asset)}}, or {{block(Device)}}.
    :cvar SPINDLE_INTERLOCK: An indication of the status of the spindle
        for a piece of equipment when power has been removed and it is
        free to rotate.
    :cvar TOOL_ASSET_ID: The identifier of an individual tool asset.
    :cvar TOOL_GROUP: An identifier for the tool group associated with a
        specific tool. Commonly used to designate spare tools.
    :cvar TOOL_ID: **DEPRECATED** in *Version 1.2.0*. See
        `TOOL_ASSET_ID`. The identifier of the tool currently in use for
        a given `Path`.
    :cvar TOOL_NUMBER: The identifier assigned by the
        {{block(Controller)}} component to a cutting tool when in use by
        a piece of equipment.
    :cvar TOOL_OFFSET: A reference to the tool offset variables applied
        to the active cutting tool associated with a {{block(Path)}} in
        a {{block(Controller)}} type component.
    :cvar USER: The identifier of the person currently responsible for
        operating the piece of equipment.
    :cvar VARIABLE: A data value whose meaning may change over time due
        to changes in the opertion of a piece of equipment or the
        process being executed on that piece of equipment.
    :cvar WAIT_STATE: An indication of the reason that
        {{block(Execution)}} is reporting a value of `WAIT`.
    :cvar WIRE: A string like piece or filament of relatively rigid or
        flexible material provided in a variety of diameters.
    :cvar WORKHOLDING_ID: The identifier for the current workholding or
        part clamp in use by a piece of equipment.
    :cvar WORK_OFFSET: A reference to the offset variables for a work
        piece or part associated with a {{block(Path)}} in a
        {{block(Controller)}} type component.
    :cvar OPERATING_SYSTEM: The Operating System of a component.
    :cvar FIRMWARE: The embedded software of a component.
    :cvar APPLICATION: The application on a component.
    :cvar LIBRARY: The software library on a component
    :cvar HARDWARE: An indication of a fault associated with the
        hardware subsystem of the {{term(Structural Element)}}.
    :cvar NETWORK: Network details of a component.
    :cvar ROTATION: A three space angular rotation relative to a
        coordinate system.
    :cvar TRANSLATION: A three space linear translation relative to a
        coordinate system.
    :cvar DEVICE_ADDED: An {{block(Event)}} that provides the
        {{term(UUID)}} of new device added to an {{term(MTConnect
        Agent)}}.
    :cvar DEVICE_REMOVED: An {{block(Event)}} that provides the
        {{term(UUID)}} of a device removed from an {{term(MTConnect
        Agent)}}.
    :cvar DEVICE_CHANGED: An {{block(Event)}} that provides the
        {{term(UUID)}} of the device whose {{term(Metadata)}} has
        changed.
    :cvar CONNECTION_STATUS: The status of the connection between an
        {{term(Adapter)}} and an {{term(Agent)}}.
    :cvar ADAPTER_SOFTWARE_VERSION: The originator’s software version of
        the {{term(Adapter)}}.
    :cvar ADAPTER_URI: The {{term(URI)}} of the {{term(Adapter)}}.
    :cvar MTCONNECT_VERSION: The reference version of the MTConnect
        Standard supported by the {{term(Adapter)}}.
    :cvar SENSOR_ATTACHMENT: An {{block(Event)}} defining an
        {{term(Attachment)}} between a sensor and an entity.
    :cvar PART_STATUS: State or condition of a part.
    :cvar PROCESS_OCCURRENCE_ID: An identifier of a process being
        executed by the device.
    :cvar PROCESS_AGGREGATE_ID: Identifier given to link the individual
        occurrence to a group of related occurrences, such as a process
        step in a process plan.
    :cvar PROCESS_KIND_ID: Identifier given to link the individual
        occurrence to a class of processes or process definition.
    :cvar PART_GROUP_ID: Identifier given to a collection of individual
        parts.
    :cvar PART_KIND_ID: Identifier given to link the individual
        occurrence to a class of parts, typically distinguished by a
        particular part design.
    :cvar PART_UNIQUE_ID: Identifier given to a distinguishable,
        individual part.
    :cvar CONTROL_LIMIT: A set of limits used to indicate whether a
        process variable is stable and in control.
    :cvar SPECIFICATION_LIMIT: A set of limits defining a range of
        values designating acceptable performance for a variable.
    :cvar ALARM_LIMIT: A set of limits used to trigger warning or alarm
        indicators.
    :cvar COMMUNICATIONS: An indication that the piece of equipment has
        experienced a communications failure.
    :cvar DATA_RANGE: An indication that the value of the data
        associated with a measured value or a calculation is outside of
        an expected range.
    :cvar LOGIC_PROGRAM: An indication that an error occurred in the
        logic program or programmable logic controller (PLC) associated
        with a piece of equipment.
    :cvar MOTION_PROGRAM: An indication that an error occurred in the
        motion program associated with a piece of equipment.
    :cvar SYSTEM: A general purpose indication associated with an
        electronic component of a piece of equipment or a controller
        that represents a fault that is not associated with the
        operator, program, or hardware.
    :cvar ACTUATOR: An indication of a fault associated with an
        actuator.
    """

    ACCELERATION = "ACCELERATION"
    ACCUMULATED_TIME = "ACCUMULATED_TIME"
    AMPERAGE = "AMPERAGE"
    ANGLE = "ANGLE"
    ANGULAR_ACCELERATION = "ANGULAR_ACCELERATION"
    ANGULAR_VELOCITY = "ANGULAR_VELOCITY"
    AXIS_FEEDRATE = "AXIS_FEEDRATE"
    CAPACITY_FLUID = "CAPACITY_FLUID"
    CAPACITY_SPATIAL = "CAPACITY_SPATIAL"
    CLOCK_TIME = "CLOCK_TIME"
    CONCENTRATION = "CONCENTRATION"
    CONDUCTIVITY = "CONDUCTIVITY"
    CUTTING_SPEED = "CUTTING_SPEED"
    DENSITY = "DENSITY"
    DEPOSITION_ACCELERATION_VOLUMETRIC = "DEPOSITION_ACCELERATION_VOLUMETRIC"
    DEPOSITION_DENSITY = "DEPOSITION_DENSITY"
    DEPOSITION_MASS = "DEPOSITION_MASS"
    DEPOSITION_RATE_VOLUMETRIC = "DEPOSITION_RATE_VOLUMETRIC"
    DEPOSITION_VOLUME = "DEPOSITION_VOLUME"
    DISPLACEMENT = "DISPLACEMENT"
    ELECTRICAL_ENERGY = "ELECTRICAL_ENERGY"
    EQUIPMENT_TIMER = "EQUIPMENT_TIMER"
    FILL_LEVEL = "FILL_LEVEL"
    FLOW = "FLOW"
    FREQUENCY = "FREQUENCY"
    GLOBAL_POSITION = "GLOBAL_POSITION"
    LENGTH = "LENGTH"
    LEVEL = "LEVEL"
    LINEAR_FORCE = "LINEAR_FORCE"
    LOAD = "LOAD"
    MASS = "MASS"
    PATH_FEEDRATE = "PATH_FEEDRATE"
    PATH_FEEDRATE_PER_REVOLUTION = "PATH_FEEDRATE_PER_REVOLUTION"
    PATH_POSITION = "PATH_POSITION"
    PH = "PH"
    POSITION = "POSITION"
    POWER_FACTOR = "POWER_FACTOR"
    PRESSURE = "PRESSURE"
    PROCESS_TIMER = "PROCESS_TIMER"
    RESISTANCE = "RESISTANCE"
    ROTARY_VELOCITY = "ROTARY_VELOCITY"
    SOUND_LEVEL = "SOUND_LEVEL"
    SPINDLE_SPEED = "SPINDLE_SPEED"
    STRAIN = "STRAIN"
    TEMPERATURE = "TEMPERATURE"
    TENSION = "TENSION"
    TILT = "TILT"
    TORQUE = "TORQUE"
    VELOCITY = "VELOCITY"
    VISCOSITY = "VISCOSITY"
    VOLTAGE = "VOLTAGE"
    VOLT_AMPERE = "VOLT_AMPERE"
    VOLT_AMPERE_REACTIVE = "VOLT_AMPERE_REACTIVE"
    VOLUME_FLUID = "VOLUME_FLUID"
    VOLUME_SPATIAL = "VOLUME_SPATIAL"
    WATTAGE = "WATTAGE"
    AMPERAGE_AC = "AMPERAGE_AC"
    AMPERAGE_DC = "AMPERAGE_DC"
    VOLTAGE_AC = "VOLTAGE_AC"
    VOLTAGE_DC = "VOLTAGE_DC"
    X_DIMENSION = "X_DIMENSION"
    Y_DIMENSION = "Y_DIMENSION"
    Z_DIMENSION = "Z_DIMENSION"
    DIAMETER = "DIAMETER"
    ORIENTATION = "ORIENTATION"
    HUMIDITY_RELATIVE = "HUMIDITY_RELATIVE"
    HUMIDITY_ABSOLUTE = "HUMIDITY_ABSOLUTE"
    HUMIDITY_SPECIFIC = "HUMIDITY_SPECIFIC"
    OBSERVATION_UPDATE_RATE = "OBSERVATION_UPDATE_RATE"
    ASSET_UPDATE_RATE = "ASSET_UPDATE_RATE"
    PRESSURIZATION_RATE = "PRESSURIZATION_RATE"
    DECELERATION = "DECELERATION"
    ANGULAR_DECELERATION = "ANGULAR_DECELERATION"
    PRESSURE_ABSOLUTE = "PRESSURE_ABSOLUTE"
    ACTIVE_AXES = "ACTIVE_AXES"
    ACTUATOR_STATE = "ACTUATOR_STATE"
    ALARM = "ALARM"
    ASSET_CHANGED = "ASSET_CHANGED"
    ASSET_REMOVED = "ASSET_REMOVED"
    AVAILABILITY = "AVAILABILITY"
    AXIS_COUPLING = "AXIS_COUPLING"
    AXIS_FEEDRATE_OVERRIDE = "AXIS_FEEDRATE_OVERRIDE"
    AXIS_INTERLOCK = "AXIS_INTERLOCK"
    AXIS_STATE = "AXIS_STATE"
    BLOCK = "BLOCK"
    BLOCK_COUNT = "BLOCK_COUNT"
    CHUCK_INTERLOCK = "CHUCK_INTERLOCK"
    CHUCK_STATE = "CHUCK_STATE"
    CLOSE_CHUCK = "CLOSE_CHUCK"
    CLOSE_DOOR = "CLOSE_DOOR"
    CODE = "CODE"
    COMPOSITION_STATE = "COMPOSITION_STATE"
    CONTROLLER_MODE = "CONTROLLER_MODE"
    CONTROLLER_MODE_OVERRIDE = "CONTROLLER_MODE_OVERRIDE"
    COUPLED_AXES = "COUPLED_AXES"
    DATE_CODE = "DATE_CODE"
    DEVICE_UUID = "DEVICE_UUID"
    DIRECTION = "DIRECTION"
    DOOR_STATE = "DOOR_STATE"
    EMERGENCY_STOP = "EMERGENCY_STOP"
    END_OF_BAR = "END_OF_BAR"
    EQUIPMENT_MODE = "EQUIPMENT_MODE"
    EXECUTION = "EXECUTION"
    FUNCTIONAL_MODE = "FUNCTIONAL_MODE"
    HARDNESS = "HARDNESS"
    INTERFACE_STATE = "INTERFACE_STATE"
    LINE = "LINE"
    LINE_LABEL = "LINE_LABEL"
    LINE_NUMBER = "LINE_NUMBER"
    MATERIAL = "MATERIAL"
    MATERIAL_CHANGE = "MATERIAL_CHANGE"
    MATERIAL_FEED = "MATERIAL_FEED"
    MATERIAL_LAYER = "MATERIAL_LAYER"
    MATERIAL_LOAD = "MATERIAL_LOAD"
    MATERIAL_RETRACT = "MATERIAL_RETRACT"
    MATERIAL_UNLOAD = "MATERIAL_UNLOAD"
    MESSAGE = "MESSAGE"
    OPEN_CHUCK = "OPEN_CHUCK"
    OPEN_DOOR = "OPEN_DOOR"
    OPERATOR_ID = "OPERATOR_ID"
    PALLET_ID = "PALLET_ID"
    PART_CHANGE = "PART_CHANGE"
    PART_COUNT = "PART_COUNT"
    PART_DETECT = "PART_DETECT"
    PART_ID = "PART_ID"
    PART_NUMBER = "PART_NUMBER"
    PATH_FEEDRATE_OVERRIDE = "PATH_FEEDRATE_OVERRIDE"
    PATH_MODE = "PATH_MODE"
    POWER_STATE = "POWER_STATE"
    POWER_STATUS = "POWER_STATUS"
    PROCESS_TIME = "PROCESS_TIME"
    PROGRAM = "PROGRAM"
    PROGRAM_COMMENT = "PROGRAM_COMMENT"
    PROGRAM_EDIT = "PROGRAM_EDIT"
    PROGRAM_EDIT_NAME = "PROGRAM_EDIT_NAME"
    PROGRAM_HEADER = "PROGRAM_HEADER"
    PROGRAM_LOCATION = "PROGRAM_LOCATION"
    PROGRAM_LOCATION_TYPE = "PROGRAM_LOCATION_TYPE"
    PROGRAM_NEST_LEVEL = "PROGRAM_NEST_LEVEL"
    ROTARY_MODE = "ROTARY_MODE"
    ROTARY_VELOCITY_OVERRIDE = "ROTARY_VELOCITY_OVERRIDE"
    SERIAL_NUMBER = "SERIAL_NUMBER"
    SPINDLE_INTERLOCK = "SPINDLE_INTERLOCK"
    TOOL_ASSET_ID = "TOOL_ASSET_ID"
    TOOL_GROUP = "TOOL_GROUP"
    TOOL_ID = "TOOL_ID"
    TOOL_NUMBER = "TOOL_NUMBER"
    TOOL_OFFSET = "TOOL_OFFSET"
    USER = "USER"
    VARIABLE = "VARIABLE"
    WAIT_STATE = "WAIT_STATE"
    WIRE = "WIRE"
    WORKHOLDING_ID = "WORKHOLDING_ID"
    WORK_OFFSET = "WORK_OFFSET"
    OPERATING_SYSTEM = "OPERATING_SYSTEM"
    FIRMWARE = "FIRMWARE"
    APPLICATION = "APPLICATION"
    LIBRARY = "LIBRARY"
    HARDWARE = "HARDWARE"
    NETWORK = "NETWORK"
    ROTATION = "ROTATION"
    TRANSLATION = "TRANSLATION"
    DEVICE_ADDED = "DEVICE_ADDED"
    DEVICE_REMOVED = "DEVICE_REMOVED"
    DEVICE_CHANGED = "DEVICE_CHANGED"
    CONNECTION_STATUS = "CONNECTION_STATUS"
    ADAPTER_SOFTWARE_VERSION = "ADAPTER_SOFTWARE_VERSION"
    ADAPTER_URI = "ADAPTER_URI"
    MTCONNECT_VERSION = "MTCONNECT_VERSION"
    SENSOR_ATTACHMENT = "SENSOR_ATTACHMENT"
    PART_STATUS = "PART_STATUS"
    PROCESS_OCCURRENCE_ID = "PROCESS_OCCURRENCE_ID"
    PROCESS_AGGREGATE_ID = "PROCESS_AGGREGATE_ID"
    PROCESS_KIND_ID = "PROCESS_KIND_ID"
    PART_GROUP_ID = "PART_GROUP_ID"
    PART_KIND_ID = "PART_KIND_ID"
    PART_UNIQUE_ID = "PART_UNIQUE_ID"
    CONTROL_LIMIT = "CONTROL_LIMIT"
    SPECIFICATION_LIMIT = "SPECIFICATION_LIMIT"
    ALARM_LIMIT = "ALARM_LIMIT"
    COMMUNICATIONS = "COMMUNICATIONS"
    DATA_RANGE = "DATA_RANGE"
    LOGIC_PROGRAM = "LOGIC_PROGRAM"
    MOTION_PROGRAM = "MOTION_PROGRAM"
    SYSTEM = "SYSTEM"
    ACTUATOR = "ACTUATOR"


class DataItemResetValueEnum(Enum):
    """
    The reset intervals.

    :cvar ACTION_COMPLETE: The value of the {{term(Data Item)}} that is
        measuring an action or operation is to be reset upon completion
        of that action or operation.
    :cvar ANNUAL: The value of the {{term(Data Item)}} is to be reset at
        the end of a 12-month period.
    :cvar DAY: The value of the {{term(Data Item)}} is to be reset at
        the end of a 24-hour period.
    :cvar LIFE: The value of the {{term(Data Item)}} is not reset and
        accumulates for the entire life of the piece of equipment.
    :cvar MAINTENANCE: The value of the {{term(Data Item)}} is to be
        reset upon completion of a maintenance event.
    :cvar MONTH: The value of the {{term(Data Item)}} is to be reset at
        the end of a monthly period.
    :cvar POWER_ON: The value of the {{term(Data Item)}} is to be reset
        when power was applied to the piece of equipment after a planned
        or unplanned interruption of power has occurred.
    :cvar SHIFT: The value of the {{term(Data Item)}} is to be reset at
        the end of a work shift.
    :cvar WEEK: The value of the {{term(Data Item)}} is to be reset at
        the end of a 7-day period.
    """

    ACTION_COMPLETE = "ACTION_COMPLETE"
    ANNUAL = "ANNUAL"
    DAY = "DAY"
    LIFE = "LIFE"
    MAINTENANCE = "MAINTENANCE"
    MONTH = "MONTH"
    POWER_ON = "POWER_ON"
    SHIFT = "SHIFT"
    WEEK = "WEEK"


class DataItemStatisticsEnum(Enum):
    """
    Statistical operations on data.

    :cvar AVERAGE: Mathematical Average value calculated for the data
        item during the calculation period.
    :cvar KURTOSIS: **DEPRECATED** in *Version 1.6*. ~~A measure of the
        "peakedness" of a probability distribution; i.e., the shape of
        the distribution curve.~~
    :cvar MAXIMUM: Maximum or peak value recorded for the data item
        during the calculation period.
    :cvar MEDIAN: The middle number of a series of numbers.
    :cvar MINIMUM: Minimum value recorded for the data item during the
        calculation period.
    :cvar MODE: The number in a series of numbers that occurs most
        often.
    :cvar RANGE: Difference between the maximum and minimum value of a
        data item during the calculation period. Also represents Peak-
        to-Peak measurement in a waveform.
    :cvar ROOT_MEAN_SQUARE: Mathematical Root Mean Square (RMS) value
        calculated for the data item during the calculation period.
    :cvar STANDARD_DEVIATION: Statistical Standard Deviation value
        calculated for the data item during the calculation period.
    """

    AVERAGE = "AVERAGE"
    KURTOSIS = "KURTOSIS"
    MAXIMUM = "MAXIMUM"
    MEDIAN = "MEDIAN"
    MINIMUM = "MINIMUM"
    MODE = "MODE"
    RANGE = "RANGE"
    ROOT_MEAN_SQUARE = "ROOT_MEAN_SQUARE"
    STANDARD_DEVIATION = "STANDARD_DEVIATION"


class DataItemSubEnumEnum(Enum):
    """
    The sub-types for a measurement.

    :cvar ABSOLUTE: Relating to or derived in the simplest manner from
        the fundamental units or measurements.
    :cvar ACTION: An indication of the operating state of a mechanism.
    :cvar ACTUAL: The measured value.
    :cvar ALL: The number of parts produced.
    :cvar ALTERNATING: The measurement of alternating voltage or
        current. If not specified further in statistic, defaults to RMS
        voltage.
    :cvar A_SCALE: A Scale weighting factor.
    :cvar AUXILIARY: When multiple locations on a piece of bar stock
        being feed by a bar feeder are referenced as the indication of
        whether the end of that piece of bar stock has been reached.
    :cvar BAD: The number of parts produced that do not conform to
        specification.
    :cvar BRINELL: A scale to measure the resistance to deformation of a
        surface.
    :cvar B_SCALE: B Scale weighting factor.
    :cvar COMMANDED: The commanded value.
    :cvar CONSUMED: The amount of material consumed from an object or
        container during a manufacturing process.
    :cvar CONTROL: The state of the enabling signal or control logic
        that enables or disables the function or operation of the
        structural element.
    :cvar C_SCALE: C Scale weighting factor.
    :cvar DELAY: A piece of equipment or process waiting for an event or
        an action to occur.
    :cvar DIRECT: The measurement of DC current or voltage.
    :cvar DRY_RUN: A setting or operator selection used to execute a
        test mode to confirm the execution of machine functions.
    :cvar D_SCALE: D Scale weighting factor.
    :cvar EXPIRATION: The time and date code relating to the expiration
        or end of useful life for a material or other physical item.
    :cvar FIRST_USE: The time and date code relating the first use of a
        material or other physical item.
    :cvar GOOD: The number of parts produced that conform to
        specification.
    :cvar INCREMENTAL: Relating to or derived from the last
        {{term(observation)}}.
    :cvar JOG: The feedrate specified by a logic or motion program when
        operating in a manual state or method (jogging).
    :cvar LATERAL: An indication of the position of a mechanism that may
        move in a lateral direction.
    :cvar LEEB: A scale to measure the elasticity of a surface.
    :cvar LENGTH: A reference to a length type tool offset variable.
    :cvar LINE: The state of the power source.
    :cvar LINEAR: The direction of motion of a linear motion.
    :cvar LOADED: Subparts of a piece of equipment are under load.
    :cvar MACHINE_AXIS_LOCK: A setting or operator selection that
        changes the behavior of the controller on a piece of equipment.
    :cvar MAIN: Relating to the primary logic or motion program
        currently being executed.
    :cvar MAINTENANCE: Relating to maintenance on the piece of
        equipment.
    :cvar MANUAL_UNCLAMP: An indication of the state of an operator
        controlled interlock that can inhibit the ability to initiate an
        unclamp action of an electronically controlled chuck.
    :cvar MANUFACTURE: Related to the production of a material or other
        physical item.
    :cvar MAXIMUM: The maximum value.
    :cvar MINIMUM: The minimum value.
    :cvar MOHS: A scale to measure the resistance to scratching of a
        surface.
    :cvar MOTION: An indication of the open or closed state of a
        mechanism.
    :cvar NO_SCALE: No weighting factor on the frequency scale.
    :cvar OPERATING: A piece of equipment that is powered or performing
        any activity.
    :cvar OPERATOR: Relating to the person currently responsible for
        operating the piece of equipment.
    :cvar OPTIONAL_STOP: A setting or operator selection that changes
        the behavior of the controller on a piece of equipment.
    :cvar OVERRIDE: The overridden value.
    :cvar POWERED: A piece of equipment is powered and functioning or
        {{termplural(Component)}} that are required to remain on are
        powered.
    :cvar PRIMARY: The main or most important location **MUST** be
        designated as the end of a piece of bar stock.
    :cvar PROBE: The value provided by a measurement probe.
    :cvar PROCESS: Relating to production of a part or product on a
        piece of equipment.
    :cvar PROGRAMMED: The programmed value.
    :cvar RADIAL: A reference to a radial type tool offset variable.
    :cvar RAPID: The feedrate specified by a logic or motion program
        when operating in a rapid positioning mode.
    :cvar REMAINING: The remaining measure of an object or an action.
    :cvar ROCKWELL: A scale to measure the resistance to deformation of
        a surface.
    :cvar ROTARY: The direction of a rotary motion using the right hand
        rule convention.
    :cvar SCHEDULE: The identity of a control program that is used to
        specify the order of execution of other programs.
    :cvar SET_UP: Relating to the preparation of a piece of equipment
        for production or restoring the piece of equipment to a neutral
        state after production.
    :cvar SHORE: A scale to measure the resistance to deformation of a
        surface.
    :cvar SINGLE_BLOCK: A setting or operator selection that changes the
        behavior of the controller on a piece of equipment.
    :cvar STANDARD: The standard measure of an object or an action.
    :cvar START: Relating to the beginning of an activity or event.
    :cvar SWITCHED: An indication of the activation state of a mechanism
        represented by a {{term(Composition)}}.
    :cvar TARGET: The targeted or desired value.
    :cvar TARGET_COMPLETION: Relating to the end or completion of an
        activity or event.
    :cvar TOOL_CHANGE_STOP: A setting or operator selection that changes
        the behavior of the controller on a piece of equipment.
    :cvar USEABLE: The remaining usable measure of an object or action.
    :cvar VERTICAL: An indication of the position of a mechanism that
        may move in a vertical direction.
    :cvar VICKERS: A scale to measure the resistance to deformation of a
        surface.
    :cvar WORKING: A piece of equipment performing any activity, the
        equipment is active and performing a function under load or not.
    :cvar IPV4_ADDRESS: The IPV4 network address of the component.
    :cvar IPV6_ADDRESS: The IPV6 network address of the component.
    :cvar GATEWAY: The Gateway for the component network.
    :cvar SUBNET_MASK: The SubNet mask for the component network.
    :cvar VLAN_ID: The layer2 Virtual Local Network (VLAN) ID for the
        component network.
    :cvar MAC_ADDRESS: Media Access Control Address. The unique physical
        address of the network hardware.
    :cvar WIRELESS: Identifies whether the connection type is wireless.
    :cvar LICENSE: The license code to validate or activate the hardware
        or software.
    :cvar VERSION: The version of the hardware or software.
    :cvar RELEASE_DATE: The date the hardware or software was released
        for general use.
    :cvar INSTALL_DATE: The date the hardware or software was installed.
    :cvar MANUFACTURER: The corporate identity for the maker of the
        hardware or software.
    :cvar UUID: The globally unique identifier as specified in ISO 11578
        or RFC 4122.
    :cvar SERIAL_NUMBER: A serial number that uniquely identifies a
        specific part.
    :cvar RAW_MATERIAL: A singular piece of material.
    :cvar LOT: A group of parts tracked as a lot.
    :cvar BATCH: A group of parts produced in a batch.
    :cvar HEAT_TREAT: A material heat number.
    :cvar PART_NUMBER: A particular part design or model.
    :cvar PART_FAMILY: A group of parts having similarities in geometry,
        manufacturing process, and/or functions.
    :cvar PART_NAME: A word or set of words by which a part is known,
        addressed, or referred to.
    :cvar PROCESS_STEP: A step in the process plan that this occurrence
        corresponds to.
    :cvar PROCESS_PLAN: A process plan that a process occurrence belongs
        to.
    :cvar ORDER_NUMBER: The authorization of a process occurrence.
    :cvar PROCESS_NAME: A word or set of words by which a process being
        executed (process occurrence) by the device is known, addressed,
        or referred to.
    :cvar ISO_STEP_EXECUTABLE: A reference to a ISO 10303 Executable.
    :cvar COMPLETE: Associated with the completion of an activity or
        event.
    :cvar ACTIVE: Relating to logic or motion program currently
        executing.
    """

    ABSOLUTE = "ABSOLUTE"
    ACTION = "ACTION"
    ACTUAL = "ACTUAL"
    ALL = "ALL"
    ALTERNATING = "ALTERNATING"
    A_SCALE = "A_SCALE"
    AUXILIARY = "AUXILIARY"
    BAD = "BAD"
    BRINELL = "BRINELL"
    B_SCALE = "B_SCALE"
    COMMANDED = "COMMANDED"
    CONSUMED = "CONSUMED"
    CONTROL = "CONTROL"
    C_SCALE = "C_SCALE"
    DELAY = "DELAY"
    DIRECT = "DIRECT"
    DRY_RUN = "DRY_RUN"
    D_SCALE = "D_SCALE"
    EXPIRATION = "EXPIRATION"
    FIRST_USE = "FIRST_USE"
    GOOD = "GOOD"
    INCREMENTAL = "INCREMENTAL"
    JOG = "JOG"
    LATERAL = "LATERAL"
    LEEB = "LEEB"
    LENGTH = "LENGTH"
    LINE = "LINE"
    LINEAR = "LINEAR"
    LOADED = "LOADED"
    MACHINE_AXIS_LOCK = "MACHINE_AXIS_LOCK"
    MAIN = "MAIN"
    MAINTENANCE = "MAINTENANCE"
    MANUAL_UNCLAMP = "MANUAL_UNCLAMP"
    MANUFACTURE = "MANUFACTURE"
    MAXIMUM = "MAXIMUM"
    MINIMUM = "MINIMUM"
    MOHS = "MOHS"
    MOTION = "MOTION"
    NO_SCALE = "NO_SCALE"
    OPERATING = "OPERATING"
    OPERATOR = "OPERATOR"
    OPTIONAL_STOP = "OPTIONAL_STOP"
    OVERRIDE = "OVERRIDE"
    POWERED = "POWERED"
    PRIMARY = "PRIMARY"
    PROBE = "PROBE"
    PROCESS = "PROCESS"
    PROGRAMMED = "PROGRAMMED"
    RADIAL = "RADIAL"
    RAPID = "RAPID"
    REMAINING = "REMAINING"
    ROCKWELL = "ROCKWELL"
    ROTARY = "ROTARY"
    SCHEDULE = "SCHEDULE"
    SET_UP = "SET_UP"
    SHORE = "SHORE"
    SINGLE_BLOCK = "SINGLE_BLOCK"
    STANDARD = "STANDARD"
    START = "START"
    SWITCHED = "SWITCHED"
    TARGET = "TARGET"
    TARGET_COMPLETION = "TARGET_COMPLETION"
    TOOL_CHANGE_STOP = "TOOL_CHANGE_STOP"
    USEABLE = "USEABLE"
    VERTICAL = "VERTICAL"
    VICKERS = "VICKERS"
    WORKING = "WORKING"
    IPV4_ADDRESS = "IPV4_ADDRESS"
    IPV6_ADDRESS = "IPV6_ADDRESS"
    GATEWAY = "GATEWAY"
    SUBNET_MASK = "SUBNET_MASK"
    VLAN_ID = "VLAN_ID"
    MAC_ADDRESS = "MAC_ADDRESS"
    WIRELESS = "WIRELESS"
    LICENSE = "LICENSE"
    VERSION = "VERSION"
    RELEASE_DATE = "RELEASE_DATE"
    INSTALL_DATE = "INSTALL_DATE"
    MANUFACTURER = "MANUFACTURER"
    UUID = "UUID"
    SERIAL_NUMBER = "SERIAL_NUMBER"
    RAW_MATERIAL = "RAW_MATERIAL"
    LOT = "LOT"
    BATCH = "BATCH"
    HEAT_TREAT = "HEAT_TREAT"
    PART_NUMBER = "PART_NUMBER"
    PART_FAMILY = "PART_FAMILY"
    PART_NAME = "PART_NAME"
    PROCESS_STEP = "PROCESS_STEP"
    PROCESS_PLAN = "PROCESS_PLAN"
    ORDER_NUMBER = "ORDER_NUMBER"
    PROCESS_NAME = "PROCESS_NAME"
    ISO_STEP_EXECUTABLE = "ISO_STEP_EXECUTABLE"
    COMPLETE = "COMPLETE"
    ACTIVE = "ACTIVE"


class DoorStateValueType(Enum):
    """
    Controlled vocabulary for DoorState.

    :cvar OPEN: A component is open to the point of a positive
        confirmation.
    :cvar CLOSED: A component is closed to the point of a positive
        confirmation.
    :cvar UNLATCHED: An intermediate position.
    :cvar UNAVAILABLE: Value is indeterminate
    """

    OPEN = "OPEN"
    CLOSED = "CLOSED"
    UNLATCHED = "UNLATCHED"
    UNAVAILABLE = "UNAVAILABLE"


class EmergencyStopValueType(Enum):
    """
    Controlled vocabulary for EmergencyStop.

    :cvar ARMED: The emergency stop circuit is complete and the piece of
        equipment, component, or composition element is allowed to
        operate.
    :cvar TRIGGERED: The operation of the piece of equipment, component,
        or composition element is inhibited.
    :cvar UNAVAILABLE: Value is indeterminate
    """

    ARMED = "ARMED"
    TRIGGERED = "TRIGGERED"
    UNAVAILABLE = "UNAVAILABLE"


class EndOfBarValueType(Enum):
    """
    Controlled vocabulary for EndOfBar.

    :cvar YES: The {{block(END_OF_BAR)}} has been reached.
    :cvar NO: The {{block(END_OF_BAR)}} has not been reached.
    :cvar UNAVAILABLE: Value is indeterminate
    """

    YES = "YES"
    NO = "NO"
    UNAVAILABLE = "UNAVAILABLE"


@dataclass
class EntryType:
    """
    See {{sect(TableEntry)}} for details on `Entry` element for {{block(Table)}}.

    :ivar key: the key
    :ivar removed: an indicatore that the entry has been removed
    :ivar content:
    """

    key: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    removed: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


class EquipmentModeValueType(Enum):
    """
    Controlled vocabulary for EquipmentMode.

    :cvar ON: On state or value.
    :cvar OFF: Off state or value.
    :cvar UNAVAILABLE: Value is indeterminate
    """

    ON = "ON"
    OFF = "OFF"
    UNAVAILABLE = "UNAVAILABLE"


class ExecutionValueType(Enum):
    """
    Controlled vocabulary for Execution.

    :cvar READY: A component is ready to engage.
    :cvar ACTIVE: The value of the {{term(Data Entity)}} that is
        engaging.
    :cvar INTERRUPTED: The action of a {{block(Component)}} has been
        suspended due to an external signal.
    :cvar FEED_HOLD: Motion of a {{block(Component)}} has been commanded
        to stop at its current position.
    :cvar STOPPED: The component is stopped.
    :cvar OPTIONAL_STOP: The controllers program has been intentionally
        stopped
    :cvar PROGRAM_STOPPED: The execution of the {{block(Controller)}}'s
        program has been stopped by a command from within the program.
    :cvar PROGRAM_COMPLETED: The execution of the controllers program
        has been stopped by a command from within the program.
    :cvar UNAVAILABLE: Value is indeterminate
    """

    READY = "READY"
    ACTIVE = "ACTIVE"
    INTERRUPTED = "INTERRUPTED"
    FEED_HOLD = "FEED_HOLD"
    STOPPED = "STOPPED"
    OPTIONAL_STOP = "OPTIONAL_STOP"
    PROGRAM_STOPPED = "PROGRAM_STOPPED"
    PROGRAM_COMPLETED = "PROGRAM_COMPLETED"
    UNAVAILABLE = "UNAVAILABLE"


class FunctionalModeValueType(Enum):
    """
    Controlled vocabulary for FunctionalMode.

    :cvar PRODUCTION: A {{term(Structural Element)}} is currently
        producing product.
    :cvar SETUP: A {{term(Structural Element)}} is being prepared or
        modified to begin production of product.
    :cvar TEARDOWN: Typically, a {{term(Structural Element)}} has
        completed the production of a product and is being modified or
        returned to a neutral state such that it may then be prepared to
        begin production of a different product.
    :cvar MAINTENANCE: Action related to maintenance on the piece of
        equipment.
    :cvar PROCESS_DEVELOPMENT: A {{term(Structural Element)}} is being
        used to prove-out a new process.
    :cvar UNAVAILABLE: Value is indeterminate
    """

    PRODUCTION = "PRODUCTION"
    SETUP = "SETUP"
    TEARDOWN = "TEARDOWN"
    MAINTENANCE = "MAINTENANCE"
    PROCESS_DEVELOPMENT = "PROCESS_DEVELOPMENT"
    UNAVAILABLE = "UNAVAILABLE"


@dataclass
class HeaderType:
    """
    Supplemental data usually placed at the beginning of a {{term(Document)}}.

    :ivar value:
    :ivar version: unique identifier of the administered item.
        {{cite(ISO/IEC 11179-:2015)}}
    :ivar creation_time: The time the file was created.
    :ivar test_indicator: Indicates that this was a test document
    :ivar instance_id: The unique instance identifier of this agent
        process
    :ivar sender: The sender of the message
    :ivar device_model_change_time: A timestamp in 8601 format of the
        last update of the Device information for any device
    :ivar buffer_size: The size of the agent's buffer.
    :ivar next_sequence: The next sequence number for subsequent
        requests
    :ivar last_sequence: The last sequence number available from the
        agent
    :ivar first_sequence: The first sequence number available from the
        agent
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    creation_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "creationTime",
            "type": "Attribute",
            "required": True,
        },
    )
    test_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "testIndicator",
            "type": "Attribute",
        },
    )
    instance_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "instanceId",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
            "max_exclusive": 18446744073709551615,
        },
    )
    sender: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    device_model_change_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "deviceModelChangeTime",
            "type": "Attribute",
            "required": True,
        },
    )
    buffer_size: Optional[int] = field(
        default=None,
        metadata={
            "name": "bufferSize",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
            "max_exclusive": 4294967295,
        },
    )
    next_sequence: Optional[int] = field(
        default=None,
        metadata={
            "name": "nextSequence",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
            "max_exclusive": 18446744073709551615,
        },
    )
    last_sequence: Optional[int] = field(
        default=None,
        metadata={
            "name": "lastSequence",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
            "max_exclusive": 18446744073709551615,
        },
    )
    first_sequence: Optional[int] = field(
        default=None,
        metadata={
            "name": "firstSequence",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
            "max_exclusive": 18446744073709551615,
        },
    )


class InterfaceEventValuesType(Enum):
    """
    The possible values for an interface event.

    :cvar UNAVAILABLE: The value is unavailable
    :cvar NOT_READY: The interface is not ready
    :cvar READY: The interface is ready
    :cvar ACTIVE: The interface is actively executing
    :cvar COMPLETE: The interface has completed the action
    :cvar FAIL: The interface action has failed
    """

    UNAVAILABLE = "UNAVAILABLE"
    NOT_READY = "NOT_READY"
    READY = "READY"
    ACTIVE = "ACTIVE"
    COMPLETE = "COMPLETE"
    FAIL = "FAIL"


class InterfaceStateValueType(Enum):
    """
    Controlled vocabulary for InterfaceState.

    :cvar ENABLED: A component is currently operational and performing
        as expected.
    :cvar DISABLED: A component is currently not operational.
    :cvar UNAVAILABLE: Value is indeterminate
    """

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"
    UNAVAILABLE = "UNAVAILABLE"


class NotifcationCodeType(Enum):
    """DEPRECATED: Types of Notifcations

    :cvar FAILURE: A failure
    :cvar FAULT: A fault occurred
    :cvar CRASH: A spindle crash
    :cvar JAM: A component has jammed
    :cvar OVERLOAD: The component has been overloaded
    :cvar ESTOP: E-Stop was pushed
    :cvar MATERIAL: A material failure has occurred
    :cvar MESSAGE: An operators message. Used with INFO severity
    :cvar OTHER: Another Notifcation type
    """

    FAILURE = "FAILURE"
    FAULT = "FAULT"
    CRASH = "CRASH"
    JAM = "JAM"
    OVERLOAD = "OVERLOAD"
    ESTOP = "ESTOP"
    MATERIAL = "MATERIAL"
    MESSAGE = "MESSAGE"
    OTHER = "OTHER"


class PartDetectValueType(Enum):
    """
    Controlled vocabulary for PartDetect.

    :cvar PRESENT: If a part or work piece has been detected or is
        present.
    :cvar NOT_PRESENT: If a part or work piece is not detected or is not
        present.
    :cvar UNAVAILABLE: Value is indeterminate
    """

    PRESENT = "PRESENT"
    NOT_PRESENT = "NOT_PRESENT"
    UNAVAILABLE = "UNAVAILABLE"


class PartStatusValueType(Enum):
    """
    Controlled vocabulary for PartStatus.

    :cvar PASS: The part does conform to given requirements.
    :cvar FAIL: The part does not conform to some given requirements.
    :cvar UNAVAILABLE: Value is indeterminate
    """

    PASS = "PASS"
    FAIL = "FAIL"
    UNAVAILABLE = "UNAVAILABLE"


class PathModeValueType(Enum):
    """
    Controlled vocabulary for PathMode.

    :cvar INDEPENDENT: The path is operating independently and without
        the influence of another path.
    :cvar MASTER: It provides information or state values that
        influences the operation of other {{block(DataItem)}} of similar
        type.
    :cvar SYNCHRONOUS: Physical or logical parts which are not
        physically connected to each other but are operating together.
    :cvar MIRROR: The axes associated with the path are mirroring the
        motion of the {{block(MASTER)}} path.
    :cvar UNAVAILABLE: Value is indeterminate
    """

    INDEPENDENT = "INDEPENDENT"
    MASTER = "MASTER"
    SYNCHRONOUS = "SYNCHRONOUS"
    MIRROR = "MIRROR"
    UNAVAILABLE = "UNAVAILABLE"


class PowerStateValueType(Enum):
    """
    Controlled vocabulary for PowerState.

    :cvar ON: On state or value.
    :cvar OFF: Off state or value.
    :cvar UNAVAILABLE: Value is indeterminate
    """

    ON = "ON"
    OFF = "OFF"
    UNAVAILABLE = "UNAVAILABLE"


class ProgramEditValueType(Enum):
    """
    Controlled vocabulary for ProgramEdit.

    :cvar ACTIVE: The value of the {{term(Data Entity)}} that is
        engaging.
    :cvar READY: A component is ready to engage.
    :cvar NOT_READY: A component is not ready to engage.
    :cvar UNAVAILABLE: Value is indeterminate
    """

    ACTIVE = "ACTIVE"
    READY = "READY"
    NOT_READY = "NOT_READY"
    UNAVAILABLE = "UNAVAILABLE"


class QualifierType(Enum):
    """
    A qualifier for the condition.

    :cvar HIGH: The value is too high
    :cvar LOW: The value is too low
    """

    HIGH = "HIGH"
    LOW = "LOW"


class RotaryModeValueType(Enum):
    """
    Controlled vocabulary for RotaryMode.

    :cvar SPINDLE: The axis is functioning as a spindle.
    :cvar INDEX: The axis is configured to index.
    :cvar CONTOUR: The position of the axis is being interpolated.
    :cvar UNAVAILABLE: Value is indeterminate
    """

    SPINDLE = "SPINDLE"
    INDEX = "INDEX"
    CONTOUR = "CONTOUR"
    UNAVAILABLE = "UNAVAILABLE"


class SeverityType(Enum):
    """DEPRECATED: The severity of the notification

    :cvar CRITICAL: The notification is critical
    :cvar ERROR: An error has occurred
    :cvar WARNING: A medium level notification that should be observed
    :cvar INFORMATION: This notification is for information purposes
        only
    """

    CRITICAL = "CRITICAL"
    ERROR = "ERROR"
    WARNING = "WARNING"
    INFORMATION = "INFORMATION"


class SpindleInterlockValueType(Enum):
    """
    Controlled vocabulary for SpindleInterlock.

    :cvar ACTIVE: The value of the {{term(Data Entity)}} that is
        engaging.
    :cvar INACTIVE: The value of the {{term(Data Entity)}} that is not
        engaging.
    :cvar UNAVAILABLE: Value is indeterminate
    """

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    UNAVAILABLE = "UNAVAILABLE"


@dataclass
class TableCellType:
    """
    A cell of a table.

    :ivar key: the key
    :ivar content:
    """

    key: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


class UnavailableValueType(Enum):
    """
    The observation value for indeterminent data.

    :cvar UNAVAILABLE: Data is unavailable
    """

    UNAVAILABLE = "UNAVAILABLE"


class WaitStateValueType(Enum):
    """
    Controlled vocabulary for WaitState.

    :cvar POWERING_UP: An indication that execution is waiting while the
        equipment is powering up and is not currently available to begin
        producing parts or products.
    :cvar POWERING_DOWN: An indication that the execution is waiting
        while the equipment is powering down but has not fully reached a
        stopped state.
    :cvar PART_LOAD: An indication that the execution is waiting while
        one or more discrete workpieces are being loaded.
    :cvar PART_UNLOAD: An indication that the execution is waiting while
        one or more discrete workpieces are being unloaded.
    :cvar TOOL_LOAD: An indication that the execution is waiting while a
        tool or tooling is being loaded.
    :cvar TOOL_UNLOAD: An indication that the execution is waiting while
        a tool or tooling is being unloaded.
    :cvar MATERIAL_LOAD: An indication that the execution is waiting
        while material is being loaded.
    :cvar MATERIAL_UNLOAD: An indication that the execution is waiting
        while material is being unloaded.
    :cvar SECONDARY_PROCESS: An indication that the execution is waiting
        while another process is completed before the execution can
        resume.
    :cvar PAUSING: An indication that the execution is waiting while the
        equipment is pausing but the piece of equipment has not yet
        reached a fully paused state.
    :cvar RESUMING: An indication that the execution is waiting while
        the equipment is resuming the production cycle but has not yet
        resumed execution.
    :cvar UNAVAILABLE: Value is indeterminate
    """

    POWERING_UP = "POWERING_UP"
    POWERING_DOWN = "POWERING_DOWN"
    PART_LOAD = "PART_LOAD"
    PART_UNLOAD = "PART_UNLOAD"
    TOOL_LOAD = "TOOL_LOAD"
    TOOL_UNLOAD = "TOOL_UNLOAD"
    MATERIAL_LOAD = "MATERIAL_LOAD"
    MATERIAL_UNLOAD = "MATERIAL_UNLOAD"
    SECONDARY_PROCESS = "SECONDARY_PROCESS"
    PAUSING = "PAUSING"
    RESUMING = "RESUMING"
    UNAVAILABLE = "UNAVAILABLE"


@dataclass
class ConditionType:
    """
    An indicator of the ability of a piece of equipment or {{term(Component)}} to
    function to specification.

    :ivar value:
    :ivar sequence: The events sequence number
    :ivar sub_type: The event subtype corresponding to the measurement
        subtype
    :ivar timestamp: The time the event occurred or recorded
    :ivar name: The name of the event corresponding to the measurement
    :ivar data_item_id: The unique identifier of the item being produced
    :ivar composition_id: The identifier of the sub-element this result
        is in reference to
    :ivar type_value: The type of either a {{term(Structural Element)}}
        or a {{block(DataItem)}} being measured.
    :ivar native_code: The component specific Notifcation code
    :ivar native_severity: The component specific Notifcation code
    :ivar qualifier: An optional attribute that helps qualify the
        condition
    :ivar statistic: The statistical operation on this data
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    sequence: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
            "max_exclusive": 18446744073709551615,
        },
    )
    sub_type: Optional[Union[DataItemSubEnumEnum, str]] = field(
        default=None,
        metadata={
            "name": "subType",
            "type": "Attribute",
            "pattern": r"[a-ln-z][a-z]*:[A-Z_0-9]+",
        },
    )
    timestamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    data_item_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "dataItemId",
            "type": "Attribute",
            "required": True,
        },
    )
    composition_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "compositionId",
            "type": "Attribute",
        },
    )
    type_value: Optional[Union[DataItemEnumEnum, str]] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-ln-z][a-z]*:[A-Z_0-9]+",
        },
    )
    native_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "nativeCode",
            "type": "Attribute",
        },
    )
    native_severity: Optional[str] = field(
        default=None,
        metadata={
            "name": "nativeSeverity",
            "type": "Attribute",
        },
    )
    qualifier: Optional[QualifierType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    statistic: Optional[Union[DataItemStatisticsEnum, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[a-ln-z][a-z]*:[A-Z_0-9]+",
        },
    )


@dataclass
class Entry(EntryType):
    """
    See {{sect(TableEntry)}} for details on `Entry` element for {{block(Table)}}.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class EventType:
    """
    Something that happens or takes place.

    :ivar sequence: The events sequence number
    :ivar sub_type: The event subtype corresponding to the measurement
        subtype
    :ivar timestamp: The time the event occurred or recorded
    :ivar name: The name of the event corresponding to the measurement
    :ivar data_item_id: The unique identifier of the item being produced
    :ivar composition_id: The identifier of the sub-element this result
        is in reference to
    :ivar reset_triggered: An optional indicator that the event or
        sample was reset
    :ivar content:
    """

    sequence: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
            "max_exclusive": 18446744073709551615,
        },
    )
    sub_type: Optional[Union[DataItemSubEnumEnum, str]] = field(
        default=None,
        metadata={
            "name": "subType",
            "type": "Attribute",
            "pattern": r"[a-ln-z][a-z]*:[A-Z_0-9]+",
        },
    )
    timestamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    data_item_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "dataItemId",
            "type": "Attribute",
            "required": True,
        },
    )
    composition_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "compositionId",
            "type": "Attribute",
        },
    )
    reset_triggered: Optional[Union[DataItemResetValueEnum, str]] = field(
        default=None,
        metadata={
            "name": "resetTriggered",
            "type": "Attribute",
            "pattern": r"[a-ln-z][a-z]*:[A-Z_0-9]+",
        },
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass
class SampleType:
    """
    The collection of one or more pieces of information.

    :ivar sequence: The events sequence number
    :ivar sub_type: The event subtype corresponding to the measurement
        subtype
    :ivar timestamp: The time the event occurred or recorded
    :ivar name: The name of the event corresponding to the measurement
    :ivar data_item_id: The unique identifier of the item being produced
    :ivar composition_id: The identifier of the sub-element this result
        is in reference to
    :ivar sample_rate: The rate the waveform was sampled at, default
        back to the value given in the data item
    :ivar reset_triggered: An optional indicator that the event or
        sample was reset
    :ivar statistic: The statistical operation on this data
    :ivar duration: The number of seconds since the reset of the
        statistic
    :ivar content:
    """

    sequence: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
            "max_exclusive": 18446744073709551615,
        },
    )
    sub_type: Optional[Union[DataItemSubEnumEnum, str]] = field(
        default=None,
        metadata={
            "name": "subType",
            "type": "Attribute",
            "pattern": r"[a-ln-z][a-z]*:[A-Z_0-9]+",
        },
    )
    timestamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    data_item_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "dataItemId",
            "type": "Attribute",
            "required": True,
        },
    )
    composition_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "compositionId",
            "type": "Attribute",
        },
    )
    sample_rate: Optional[float] = field(
        default=None,
        metadata={
            "name": "sampleRate",
            "type": "Attribute",
        },
    )
    reset_triggered: Optional[Union[DataItemResetValueEnum, str]] = field(
        default=None,
        metadata={
            "name": "resetTriggered",
            "type": "Attribute",
            "pattern": r"[a-ln-z][a-z]*:[A-Z_0-9]+",
        },
    )
    statistic: Optional[Union[DataItemStatisticsEnum, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[a-ln-z][a-z]*:[A-Z_0-9]+",
        },
    )
    duration: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass
class TableCell(TableCellType):
    """
    A cell of a table.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class TableEntryType(EntryType):
    """A {{term(key-value pair)}} published as part of a {{term(Table)}}
    {{term(observation)}}.

    Note: Represented as {{block(Entry)}} in XML.
    """


@dataclass
class ToolOffsetCellType(TableCellType):
    """
    Cell of A reference to the tool offset variables applied to the active cutting
    tool associated with a {{block(Path)}} in a {{block(Controller)}} type
    component.
    """

    content: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    value: Union[str, UnavailableValueType] = field(default="")


@dataclass
class ToolOffsetTableEntryType(EntryType):
    """
    Table Entry of A reference to the tool offset variables applied to the active
    cutting tool associated with a {{block(Path)}} in a {{block(Controller)}} type
    component.
    """


@dataclass
class VariableEntryType(EntryType):
    """
    DataSet of A data value whose meaning may change over time due to changes in
    the opertion of a piece of equipment or the process being executed on that
    piece of equipment.
    """

    content: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    value: Union[str, UnavailableValueType] = field(default="")


@dataclass
class WorkOffsetCellType(TableCellType):
    """
    Cell of A reference to the offset variables for a work piece or part associated
    with a {{block(Path)}} in a {{block(Controller)}} type component.
    """

    content: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    value: Union[str, UnavailableValueType] = field(default="")


@dataclass
class WorkOffsetTableEntryType(EntryType):
    """
    Table Entry of A reference to the offset variables for a work piece or part
    associated with a {{block(Path)}} in a {{block(Controller)}} type component.
    """


@dataclass
class AbsTimeSeriesType(SampleType):
    """
    The abstract waveform.

    :ivar sample_count: The number of samples
    """

    sample_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "sampleCount",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ActuatorStateType(EventType):
    """
    Represents the operational state of an apparatus for moving or controlling a
    mechanism or system.
    """

    content: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    value: Optional[ActuatorStateValueType] = field(default=None)


@dataclass
class AvailabilityType(EventType):
    """
    Represents the {{term(Agent)}}'s ability to communicate with the data source.
    """

    content: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    value: Optional[AvailabilityValueType] = field(default=None)


@dataclass
class AxisCouplingType(EventType):
    """Describes the way the axes will be associated to each other.

    This is used in conjunction with {{block(CoupledAxis)}} to indicate
    the way they are interacting.
    """

    content: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    value: Optional[AxisCouplingValueType] = field(default=None)


@dataclass
class AxisInterlockType(EventType):
    """
    An indicator of the state of the axis lockout function when power has been
    removed and the axis is allowed to move freely.
    """

    content: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    value: Optional[AxisInterlockValueType] = field(default=None)


@dataclass
class AxisStateType(EventType):
    """
    An indicator of the controlled state of a {{block(Linear)}} or
    {{block(Rotary)}} component representing an axis.
    """

    content: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    value: Optional[AxisStateValueType] = field(default=None)


@dataclass
class ChuckInterlockType(EventType):
    """
    An indication of the operational condition of the interlock function for an
    electronically controller chuck.
    """

    content: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    value: Optional[ChuckInterlockValueType] = field(default=None)


@dataclass
class ChuckStateType(EventType):
    """An indication of the operating state of a mechanism that holds a part or
    stock material during a manufacturing process.

    It may also represent a mechanism that holds any other mechanism in
    place within a piece of equipment.
    """

    content: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    value: Optional[ChuckStateValueType] = field(default=None)


@dataclass
class CommonSampleType(SampleType):
    """
    A sample with a single floating point value.
    """

    content: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    value: Optional[Union[float, UnavailableValueType]] = field(default=None)


@dataclass
class Condition(ConditionType):
    """
    An indicator of the ability of a piece of equipment or {{term(Component)}} to
    function to specification.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class ConnectionStatusType(EventType):
    """
    The status of the connection between an {{term(Adapter)}} and an
    {{term(Agent)}}.
    """

    content: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    value: Optional[ConnectionStatusValueType] = field(default=None)


@dataclass
class ControllerModeOverrideType(EventType):
    """
    A setting or operator selection that changes the behavior of a piece of
    equipment.
    """

    content: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    value: Optional[ControllerModeOverrideValueType] = field(default=None)


@dataclass
class ControllerModeType(EventType):
    """
    The current operating mode of the {{block(Controller)}} component.
    """

    content: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    value: Optional[ControllerModeValueType] = field(default=None)


@dataclass
class DoorStateType(EventType):
    """
    The operational state of a {{block(Door)}} type component or composition
    element.
    """

    content: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    value: Optional[DoorStateValueType] = field(default=None)


@dataclass
class EmergencyStopType(EventType):
    """
    The current state of the emergency stop signal for a piece of equipment,
    controller path, or any other component or subsystem of a piece of equipment.
    """

    content: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    value: Optional[EmergencyStopValueType] = field(default=None)


@dataclass
class EndOfBarType(EventType):
    """
    An indication that the end of a piece of bar stock has been reached.
    """

    content: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    value: Optional[EndOfBarValueType] = field(default=None)


@dataclass
class EquipmentModeType(EventType):
    """
    An indication that a piece of equipment, or a sub-part of a piece of equipment,
    is performing specific types of activities.
    """

    content: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    value: Optional[EquipmentModeValueType] = field(default=None)


@dataclass
class Event(EventType):
    """
    Something that happens or takes place.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class ExecutionType(EventType):
    """
    The execution status of the {{block(Component)}}.
    """

    content: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    value: Optional[ExecutionValueType] = field(default=None)


@dataclass
class FaultType(ConditionType):
    """
    {{block(Fault)}} indicates an unexpected situation because the value is
    unexpected or out of tolerance for the data.
    """


@dataclass
class FloatEventType(EventType):
    """
    An event with an integer value.
    """

    content: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    value: Optional[Union[float, UnavailableValueType]] = field(default=None)


@dataclass
class FunctionalModeType(EventType):
    """
    The current intended production status of the device or component.
    """

    content: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    value: Optional[FunctionalModeValueType] = field(default=None)


@dataclass
class IntegerEventType(EventType):
    """
    An event with an integer value.
    """

    content: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    value: Optional[Union[int, UnavailableValueType]] = field(default=None)


@dataclass
class InterfaceEventType(EventType):
    """
    An abstract interface event.
    """

    content: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    value: Optional[InterfaceEventValuesType] = field(default=None)


@dataclass
class InterfaceStateType(EventType):
    """
    An indication of the operation condition of an {{block(Interface)}} component.
    """

    content: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    value: Optional[InterfaceStateValueType] = field(default=None)


@dataclass
class NormalType(ConditionType):
    """
    {{block(Normal)}} indicates whether the value of the data is within an expected
    range.
    """


@dataclass
class PartDetectType(EventType):
    """
    An indication designating whether a part or work piece has been detected or is
    present.
    """

    content: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    value: Optional[PartDetectValueType] = field(default=None)


@dataclass
class PartStatusType(EventType):
    """State or condition of a part.

    If unique identifier is given, part status is for that individual.
    If group identifier is given without a unique identifier, then the
    status is assumed to be for the whole group.
    """

    content: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    value: Optional[PartStatusValueType] = field(default=None)


@dataclass
class PathModeType(EventType):
    """
    Describes the operational relationship between a {{block(Path)}}
    {{term(Structural Element)}} and another {{block(Path)}} {{term(Structural
    Element)}} for pieces of equipment comprised of multiple logical groupings of
    controlled axes or other logical operations.
    """

    content: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    value: Optional[PathModeValueType] = field(default=None)


@dataclass
class PowerStateType(EventType):
    """
    The indication of the status of the source of energy for a {{term(Structural
    Element)}} to allow it to perform its intended function or the state of an
    enabling signal providing permission for the {{term(Structural Element)}} to
    perform its functions.
    """

    content: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    value: Optional[PowerStateValueType] = field(default=None)


@dataclass
class ProgramEditType(EventType):
    """An indication of the status of the {{block(Controller)}} components program
    editing mode.

    On many controls, a program can be edited while another program is
    currently being executed.
    """

    content: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    value: Optional[ProgramEditValueType] = field(default=None)


@dataclass
class RotaryModeType(EventType):
    """
    The current operating mode for a {{block(Rotary)}} type axis.
    """

    content: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    value: Optional[RotaryModeValueType] = field(default=None)


@dataclass
class Sample(SampleType):
    """
    The collection of one or more pieces of information.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class SpindleInterlockType(EventType):
    """
    An indication of the status of the spindle for a piece of equipment when power
    has been removed and it is free to rotate.
    """

    content: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    value: Optional[SpindleInterlockValueType] = field(default=None)


@dataclass
class StringEventType(EventType):
    """
    An unfaceted string event.
    """

    content: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    value: Union[str, UnavailableValueType] = field(default="")


@dataclass
class StringListEventType(EventType):
    """
    An unfaceted string event.
    """

    content: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    value: List[Union[str, UnavailableValueType]] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )


@dataclass
class TableEntry(TableEntryType):
    """A {{term(key-value pair)}} published as part of a {{term(Table)}}
    {{term(observation)}}.

    Note: Represented as {{block(Entry)}} in XML.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class ThreeSpaceSampleType(SampleType):
    """
    A sample with a three tuple floating point value.
    """

    content: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    value: List[Union[str, UnavailableValueType]] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )


@dataclass
class ToolOffsetCell(ToolOffsetCellType):
    """
    Cell of A reference to the tool offset variables applied to the active cutting
    tool associated with a {{block(Path)}} in a {{block(Controller)}} type
    component.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class ToolOffsetTableEntry(ToolOffsetTableEntryType):
    """
    Table Entry of A reference to the tool offset variables applied to the active
    cutting tool associated with a {{block(Path)}} in a {{block(Controller)}} type
    component.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class ToolOffsetTableType(EventType):
    """
    Table of A reference to the tool offset variables applied to the active cutting
    tool associated with a {{block(Path)}} in a {{block(Controller)}} type
    component.

    :ivar count: The number of entries
    """

    count: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class UnavailableType(ConditionType):
    """
    The conditon can not be determined.
    """


@dataclass
class VariableDataSetType(EventType):
    """
    DataSet of A data value whose meaning may change over time due to changes in
    the opertion of a piece of equipment or the process being executed on that
    piece of equipment.

    :ivar count: The number of entries
    """

    count: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class VariableEntry(VariableEntryType):
    """
    DataSet of A data value whose meaning may change over time due to changes in
    the opertion of a piece of equipment or the process being executed on that
    piece of equipment.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class WaitStateType(EventType):
    """
    An indication of the reason that {{block(Execution)}} is reporting a value of
    `WAIT`.
    """

    content: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    value: Optional[WaitStateValueType] = field(default=None)


@dataclass
class WarningType(ConditionType):
    """
    {{block(Warning)}} indicates a possible unexpected situation because the value
    is unexpected or out of tolerance for the data.
    """


@dataclass
class WorkOffsetCell(WorkOffsetCellType):
    """
    Cell of A reference to the offset variables for a work piece or part associated
    with a {{block(Path)}} in a {{block(Controller)}} type component.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class WorkOffsetTableEntry(WorkOffsetTableEntryType):
    """
    Table Entry of A reference to the offset variables for a work piece or part
    associated with a {{block(Path)}} in a {{block(Controller)}} type component.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class WorkOffsetTableType(EventType):
    """
    Table of A reference to the offset variables for a work piece or part
    associated with a {{block(Path)}} in a {{block(Controller)}} type component.

    :ivar count: The number of entries
    """

    count: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class AbsTimeSeries(AbsTimeSeriesType):
    """
    The abstract waveform.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class AccelerationType(CommonSampleType):
    """
    The measurement of the rate of change of velocity.
    """


@dataclass
class AccumulatedTimeType(CommonSampleType):
    """
    The measurement of accumulated time for an activity or event.
    """


@dataclass
class ActiveAxesType(StringListEventType):
    """
    The result is a space delimited list of axes names.
    """


@dataclass
class ActuatorState(ActuatorStateType):
    """
    Represents the operational state of an apparatus for moving or controlling a
    mechanism or system.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class AdapterSoftwareVersionType(StringEventType):
    """
    The originator’s software version of the {{term(Adapter)}}.
    """


@dataclass
class AdapterUritype(StringEventType):
    """
    The {{term(URI)}} of the {{term(Adapter)}}.
    """

    class Meta:
        name = "AdapterURIType"


@dataclass
class AlarmLimitType(StringEventType):
    """
    A set of limits used to trigger warning or alarm indicators.
    """


@dataclass
class AlarmType(StringEventType):
    """
    **DEPRECATED:** Replaced with {{block(CONDITION)}} category data items in
    Version 1.1.0.

    :ivar code: **DEPRECATED** in *Version 1.1*. The programmatic code
        being executed.
    :ivar severity: The severity
    :ivar state: The state
    :ivar native_code: The component specific Notifcation code
    """

    code: Optional[NotifcationCodeType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    severity: Optional[SeverityType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    state: Optional[AlarmStateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    native_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "nativeCode",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class AmperageActype(CommonSampleType):
    """
    The measurement of an electrical current that reverses direction at regular
    short intervals.
    """

    class Meta:
        name = "AmperageACType"


@dataclass
class AmperageDctype(CommonSampleType):
    """
    The measurement of an electric current flowing in one direction only.
    """

    class Meta:
        name = "AmperageDCType"


@dataclass
class AmperageType(CommonSampleType):
    """**DEPRECATED** in *Version 1.6*.

    Replaced by {{block(AmperageAC)}} and {{block(AmperageDC)}}. The
    measurement of electrical current.
    """


@dataclass
class AngleType(CommonSampleType):
    """
    The measurement of angular position.
    """


@dataclass
class AngularAccelerationType(CommonSampleType):
    """
    The measurement rate of change of angular velocity.
    """


@dataclass
class AngularDecelerationType(CommonSampleType):
    """
    Negative rate of change of angular velocity.
    """


@dataclass
class AngularVelocityType(CommonSampleType):
    """
    The measurement of the rate of change of angular position.
    """


@dataclass
class ApplicationType(StringEventType):
    """Software or a program that is specific to the solution of an application
    problem.

    {{cite(ISO/IEC 20944-1:2013)}}
    """


@dataclass
class AssetChangedType(StringEventType):
    """An {{term(MTConnect Asset)}} has been added or modified.

    The value **MUST** be the {{property(assetId)}} of the
    {{block(Asset)}} that has been modified.

    :ivar asset_type: The type of asset
    """

    asset_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "assetType",
            "type": "Attribute",
        },
    )


@dataclass
class AssetRemovedType(StringEventType):
    """An {{term(MTConnect Asset)}} has been removed.

    The value **MUST** be the {{property(assetId)}} of the
    {{block(Asset)}} that has been removed.

    :ivar asset_type: The type of asset
    """

    asset_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "assetType",
            "type": "Attribute",
        },
    )


@dataclass
class AssetUpdateRateType(CommonSampleType):
    """The average rate of change of values for assets in the MTConnect streams.

    The average is computed over a rolling window defined by the
    implementation.
    """


@dataclass
class Availability(AvailabilityType):
    """
    Represents the {{term(Agent)}}'s ability to communicate with the data source.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class AxisCoupling(AxisCouplingType):
    """Describes the way the axes will be associated to each other.

    This is used in conjunction with {{block(CoupledAxis)}} to indicate
    the way they are interacting.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class AxisFeedrateOverrideType(FloatEventType):
    """
    The value of a signal or calculation issued to adjust the feedrate of an
    individual linear type axis.
    """


@dataclass
class AxisFeedrateType(CommonSampleType):
    """
    The measurement of the feedrate of a linear axis.
    """


@dataclass
class AxisInterlock(AxisInterlockType):
    """
    An indicator of the state of the axis lockout function when power has been
    removed and the axis is allowed to move freely.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class AxisState(AxisStateType):
    """
    An indicator of the controlled state of a {{block(Linear)}} or
    {{block(Rotary)}} component representing an axis.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class BlockCountType(IntegerEventType):
    """
    The total count of the number of blocks of program code that have been executed
    since execution started.
    """


@dataclass
class BlockType(StringEventType):
    """
    The line of code or command being executed by a {{block(Controller)}}
    {{term(Structural Element)}}.
    """


@dataclass
class CapacityFluidType(CommonSampleType):
    """
    The fluid capacity of an object or container.
    """


@dataclass
class CapacitySpatialType(CommonSampleType):
    """
    The geometric capacity of an object or container.
    """


@dataclass
class ChuckInterlock(ChuckInterlockType):
    """
    An indication of the operational condition of the interlock function for an
    electronically controller chuck.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class ChuckState(ChuckStateType):
    """An indication of the operating state of a mechanism that holds a part or
    stock material during a manufacturing process.

    It may also represent a mechanism that holds any other mechanism in
    place within a piece of equipment.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class ClockTimeType(CommonSampleType):
    """
    The value provided by a timing device at a specific point in time.
    """


@dataclass
class CloseChuckType(StringEventType):
    """
    Service to close a chuck.
    """


@dataclass
class CloseDoorType(StringEventType):
    """
    Service to close a door.
    """


@dataclass
class CodeType(StringEventType):
    """**DEPRECATED** in *Version 1.1*.

    The programmatic code being executed.
    """


@dataclass
class CommonSample(CommonSampleType):
    """
    A sample with a single floating point value.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class CompositionStateType(StringEventType):
    """
    An indication of the operating condition of a mechanism represented by a
    {{block(Composition)}} type element.
    """


@dataclass
class ConcentrationType(CommonSampleType):
    """
    The measurement of the percentage of one component within a mixture of
    components.
    """


@dataclass
class ConductivityType(CommonSampleType):
    """
    The measurement of the ability of a material to conduct electricity.
    """


@dataclass
class ConnectionStatus(ConnectionStatusType):
    """
    The status of the connection between an {{term(Adapter)}} and an
    {{term(Agent)}}.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class ControlLimitType(StringEventType):
    """
    A set of limits used to indicate whether a process variable is stable and in
    control.
    """


@dataclass
class ControllerMode(ControllerModeType):
    """
    The current operating mode of the {{block(Controller)}} component.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class ControllerModeOverride(ControllerModeOverrideType):
    """
    A setting or operator selection that changes the behavior of a piece of
    equipment.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class CoupledAxesType(StringListEventType):
    """
    Refers to the set of associated axes.
    """


@dataclass
class CuttingSpeedType(CommonSampleType):
    """
    The speed difference (relative velocity) between the cutting mechanism and the
    surface of the workpiece it is operating on.
    """


@dataclass
class DateCodeType(StringEventType):
    """The time and date code associated with a material or other physical item.

    {{block(DATE_CODE)}} **MUST** be reported in ISO 8601 format.
    """


@dataclass
class DecelerationType(CommonSampleType):
    """
    Negative rate of change of velocity.
    """


@dataclass
class DensityType(CommonSampleType):
    """
    The volumetric mass of a material per unit volume of that material.
    """


@dataclass
class DepositionAccelerationVolumetricType(CommonSampleType):
    """
    The rate of change in spatial volume of material deposited in an additive
    manufacturing process.
    """


@dataclass
class DepositionDensityType(CommonSampleType):
    """
    The density of the material deposited in an additive manufacturing process per
    unit of volume.
    """


@dataclass
class DepositionMassType(CommonSampleType):
    """
    The mass of the material deposited in an additive manufacturing process.
    """


@dataclass
class DepositionRateVolumetricType(CommonSampleType):
    """
    The rate at which a spatial volume of material is deposited in an additive
    manufacturing process.
    """


@dataclass
class DepositionVolumeType(CommonSampleType):
    """
    The spatial volume of material to be deposited in an additive manufacturing
    process.
    """


@dataclass
class DeviceAddedType(StringEventType):
    """
    An {{block(Event)}} that provides the {{term(UUID)}} of new device added to an
    {{term(MTConnect Agent)}}.
    """


@dataclass
class DeviceChangedType(StringEventType):
    """
    An {{block(Event)}} that provides the {{term(UUID)}} of the device whose
    {{term(Metadata)}} has changed.
    """


@dataclass
class DeviceRemovedType(StringEventType):
    """
    An {{block(Event)}} that provides the {{term(UUID)}} of a device removed from
    an {{term(MTConnect Agent)}}.
    """


@dataclass
class DeviceUuidType(StringEventType):
    """
    The identifier of another piece of equipment that is temporarily associated
    with a component of this piece of equipment to perform a particular function.
    """


@dataclass
class DiameterType(CommonSampleType):
    """
    The measured dimension of a diameter.
    """


@dataclass
class DirectionType(StringEventType):
    """
    An indication of a fault associated with the direction of motion of a
    {{term(Structural Element)}}.
    """


@dataclass
class DisplacementType(CommonSampleType):
    """
    The measurement of the change in position of an object.
    """


@dataclass
class DoorState(DoorStateType):
    """
    The operational state of a {{block(Door)}} type component or composition
    element.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class ElectricalEnergyType(CommonSampleType):
    """
    The measurement of electrical energy consumption by a component.
    """


@dataclass
class EmergencyStop(EmergencyStopType):
    """
    The current state of the emergency stop signal for a piece of equipment,
    controller path, or any other component or subsystem of a piece of equipment.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class EndOfBar(EndOfBarType):
    """
    An indication that the end of a piece of bar stock has been reached.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class EquipmentMode(EquipmentModeType):
    """
    An indication that a piece of equipment, or a sub-part of a piece of equipment,
    is performing specific types of activities.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class EquipmentTimerType(CommonSampleType):
    """
    The measurement of the amount of time a piece of equipment or a sub-part of a
    piece of equipment has performed specific activities.
    """


@dataclass
class Execution(ExecutionType):
    """
    The execution status of the {{block(Component)}}.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class Fault(FaultType):
    """
    {{block(Fault)}} indicates an unexpected situation because the value is
    unexpected or out of tolerance for the data.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class FillLevelType(CommonSampleType):
    """
    The measurement of the amount of a substance remaining compared to the planned
    maximum amount of that substance.
    """


@dataclass
class FirmwareType(StringEventType):
    """
    The embedded software of a component.
    """


@dataclass
class FloatEvent(FloatEventType):
    """
    An event with an integer value.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class FlowType(CommonSampleType):
    """
    The measurement of the rate of flow of a fluid.
    """


@dataclass
class FrequencyType(CommonSampleType):
    """
    The measurement of the number of occurrences of a repeating event per unit
    time.
    """


@dataclass
class FunctionalMode(FunctionalModeType):
    """
    The current intended production status of the device or component.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class GlobalPositionType(CommonSampleType):
    """
    **DEPRECATED** in Version 1.1.
    """


@dataclass
class HardnessType(FloatEventType):
    """
    The measurement of the hardness of a material.
    """


@dataclass
class HardwareType(StringEventType):
    """
    An indication of a fault associated with the hardware subsystem of the
    {{term(Structural Element)}}.
    """


@dataclass
class HumidityAbsoluteType(CommonSampleType):
    """
    The amount of water vapor expressed in grams per cubic meter.
    """


@dataclass
class HumidityRelativeType(CommonSampleType):
    """
    The amount of water vapor present expressed as a percent to reach saturation at
    the same temperature.
    """


@dataclass
class HumiditySpecificType(CommonSampleType):
    """
    The ratio of the water vapor present over the total weight of the water vapor
    and air present expressed as a percent.
    """


@dataclass
class IntegerEvent(IntegerEventType):
    """
    An event with an integer value.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class InterfaceEvent(InterfaceEventType):
    """
    An abstract interface event.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class InterfaceState(InterfaceStateType):
    """
    An indication of the operation condition of an {{block(Interface)}} component.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class LengthType(CommonSampleType):
    """
    The measurement of the length of an object.
    """


@dataclass
class LevelType(CommonSampleType):
    """**DEPRECATED** in *Version 1.2*.

    See {{block(FillLevel)}}. Represents the level of a resource.
    """


@dataclass
class LibraryType(StringEventType):
    """
    The software library on a component.
    """


@dataclass
class LineLabelType(StringEventType):
    """
    An optional identifier for a {{block(Block)}} of code in a {{block(Program)}}.
    """


@dataclass
class LineNumberType(IntegerEventType):
    """
    A reference to the position of a block of program code within a control
    program.
    """


@dataclass
class LineType(StringEventType):
    """**DEPRECATED** in *Version 1.4.0*.

    The current line of code being executed.
    """


@dataclass
class LinearForceType(CommonSampleType):
    """
    The measurement of the push or pull introduced by an actuator or exerted on an
    object.
    """


@dataclass
class LoadType(CommonSampleType):
    """
    The measurement of the actual versus the standard rating of a piece of
    equipment.
    """


@dataclass
class MtconnectVersionType(StringEventType):
    """
    The reference version of the MTConnect Standard supported by the
    {{term(Adapter)}} .
    """

    class Meta:
        name = "MTConnectVersionType"


@dataclass
class MassType(CommonSampleType):
    """
    The measurement of the mass of an object(s) or an amount of material.
    """


@dataclass
class MaterialChangeType(StringEventType):
    """
    Service to change the type of material or product being loaded or fed to a
    piece of equipment.
    """


@dataclass
class MaterialFeedType(StringEventType):
    """
    Service to advance material or feed product to a piece of equipment from a
    continuous or bulk source.
    """


@dataclass
class MaterialLayerType(IntegerEventType):
    """
    Identifies the layers of material applied to a part or product as part of an
    additive manufacturing process.
    """


@dataclass
class MaterialLoadType(StringEventType):
    """
    Service to load a piece of material or product.
    """


@dataclass
class MaterialRetractType(StringEventType):
    """
    Service to remove or retract material or product.
    """


@dataclass
class MaterialType(StringEventType):
    """
    {{block(Materials)}} provides information about materials or other items
    consumed or used by the piece of equipment for production of parts, materials,
    or other types of goods.
    """


@dataclass
class MaterialUnloadType(StringEventType):
    """
    Service to unload a piece of material or product.
    """


@dataclass
class MessageType(StringEventType):
    """
    A communication in writing, in speech, or by signals.
    """


@dataclass
class NetworkType(StringEventType):
    """
    Network details of a component.
    """


@dataclass
class Normal(NormalType):
    """
    {{block(Normal)}} indicates whether the value of the data is within an expected
    range.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class ObservationUpdateRateType(CommonSampleType):
    """The average rate of change of values for data items in the MTConnect
    streams.

    The average is computed over a rolling window defined by the
    implementation.
    """


@dataclass
class OpenChuckType(StringEventType):
    """
    Service to open a chuck.
    """


@dataclass
class OpenDoorType(StringEventType):
    """
    Service to open a door.
    """


@dataclass
class OperatingSystemType(StringEventType):
    """
    The Operating System of a component.
    """


@dataclass
class OperatorIdType(StringEventType):
    """
    The identifier of the person currently responsible for operating the piece of
    equipment.
    """


@dataclass
class OrientationType(ThreeSpaceSampleType):
    """
    A measured or calculated orientation of a plane or vector relative to a
    cartesian coordinate system.
    """


@dataclass
class Phtype(CommonSampleType):
    """
    A measure of the acidity or alkalinity of a solution.
    """

    class Meta:
        name = "PHType"


@dataclass
class PalletIdType(StringEventType):
    """
    The identifier for a pallet.
    """


@dataclass
class PartChangeType(StringEventType):
    """
    Service to change the part or product associated with a piece of equipment to a
    different part or product.
    """


@dataclass
class PartCountType(FloatEventType):
    """
    The aggregate count of parts.
    """


@dataclass
class PartDetect(PartDetectType):
    """
    An indication designating whether a part or work piece has been detected or is
    present.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class PartGroupIdType(StringEventType):
    """Identifier given to a collection of individual parts.

    If no
    {{property(subType)}} is specified, `UUID` is default.
    """


@dataclass
class PartIdType(StringEventType):
    """
    An identifier of a part in a manufacturing operation.
    """


@dataclass
class PartKindIdType(StringEventType):
    """Identifier given to link the individual occurrence to a class of parts,
    typically distinguished by a particular part design.

    If no
    {{property(subType)}} is specified, `UUID` is default.
    """


@dataclass
class PartNumberType(StringEventType):
    """**DEPRECATED** in *Version 1.7*.

    {{block(PartNumber)}} is now a
    `subType` of {{block(PartKindId)}}. An identifier of a part or product
    moving through the manufacturing process.
    """


@dataclass
class PartStatus(PartStatusType):
    """State or condition of a part.

    If unique identifier is given, part status is for that individual.
    If group identifier is given without a unique identifier, then the
    status is assumed to be for the whole group.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class PartUniqueIdType(StringEventType):
    """Identifier given to a distinguishable, individual part.

    If no
    {{property(subType)}} is specified, `UUID` is default.
    """


@dataclass
class PathFeedrateOverrideType(FloatEventType):
    """
    The value of a signal or calculation issued to adjust the feedrate for the axes
    associated with a {{block(Path)}} component that may represent a single axis or
    the coordinated movement of multiple axes.
    """


@dataclass
class PathFeedratePerRevolutionType(CommonSampleType):
    """
    The feedrate for the axes, or a single axis.
    """


@dataclass
class PathFeedrateType(CommonSampleType):
    """
    The measurement of the feedrate for the axes, or a single axis, associated with
    a {{block(Path)}} component-a vector.
    """


@dataclass
class PathMode(PathModeType):
    """
    Describes the operational relationship between a {{block(Path)}}
    {{term(Structural Element)}} and another {{block(Path)}} {{term(Structural
    Element)}} for pieces of equipment comprised of multiple logical groupings of
    controlled axes or other logical operations.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class PathPositionType(ThreeSpaceSampleType):
    """
    A measured or calculated position of a control point associated with a
    {{block(Controller)}} element, or {{block(Path)}} element if provided, of a
    piece of equipment.
    """


@dataclass
class PositionType(CommonSampleType):
    """
    A measured or calculated position of a {{block(Component)}} element as reported
    by a piece of equipment.
    """


@dataclass
class PowerFactorType(CommonSampleType):
    """
    The measurement of the ratio of real power flowing to a load to the apparent
    power in that AC circuit.
    """


@dataclass
class PowerState(PowerStateType):
    """
    The indication of the status of the source of energy for a {{term(Structural
    Element)}} to allow it to perform its intended function or the state of an
    enabling signal providing permission for the {{term(Structural Element)}} to
    perform its functions.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class PowerStatusType(StringEventType):
    """**DEPRECATED** in *Version 1.1.0*.

    The `ON` or `OFF` status of the
    component.
    """


@dataclass
class PressureAbsoluteType(CommonSampleType):
    """
    The force per unit area measured relative to a vacuum.
    """


@dataclass
class PressureType(CommonSampleType):
    """{{block(Pressure)}} is a system that delivers compressed gas or fluid and
    controls the pressure and rate of pressure change to a desired target set-
    point.

    Note: For example, Delivery Method can be a Compressed
    Air or N2 tank that is piped via an inlet valve to the chamber.
    """


@dataclass
class PressurizationRateType(CommonSampleType):
    """
    The change of pressure per unit time.
    """


@dataclass
class ProcessAggregateIdType(StringEventType):
    """
    Identifier given to link the individual occurrence to a group of related
    occurrences, such as a process step in a process plan.
    """


@dataclass
class ProcessKindIdType(StringEventType):
    """
    Identifier given to link the individual occurrence to a class of processes or
    process definition.
    """


@dataclass
class ProcessOccurrenceIdType(StringEventType):
    """
    An identifier of a process being executed by the device.
    """


@dataclass
class ProcessTimeType(StringEventType):
    """The time and date associated with an activity or event.

    {{block(ProcessTime)}} **MUST** be reported in ISO 8601 format.
    """


@dataclass
class ProcessTimerType(CommonSampleType):
    """
    The measurement of the amount of time a piece of equipment has performed
    different types of activities associated with the process being performed at
    that piece of equipment.
    """


@dataclass
class ProgramCommentType(StringEventType):
    """
    A comment or non-executable statement in the control program.
    """


@dataclass
class ProgramEdit(ProgramEditType):
    """An indication of the status of the {{block(Controller)}} components program
    editing mode.

    On many controls, a program can be edited while another program is
    currently being executed.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class ProgramEditNameType(StringEventType):
    """The name of the program being edited.

    This is used in conjunction with
    {{block(ProgramEdit)}} when in `ACTIVE` state.
    """


@dataclass
class ProgramHeaderType(StringEventType):
    """
    The non-executable header section of the control program.
    """


@dataclass
class ProgramLocationTypeType(StringEventType):
    """
    Defines whether the logic or motion program defined by {{block(Program)}} is
    being executed from the local memory of the controller or from an outside
    source.
    """


@dataclass
class ProgramLocationType1(StringEventType):
    """
    The Uniform Resource Identifier (URI) for the source file associated with
    {{block(Program)}}.
    """

    class Meta:
        name = "ProgramLocationType"


@dataclass
class ProgramNestLevelType(IntegerEventType):
    """An indication of the nesting level within a control program that is
    associated with the code or instructions that is currently being executed.

    If an Initial Value is not defined, the nesting level associated
    with the highest or initial nesting level of the program **MUST**
    default to zero (0).
    """


@dataclass
class ProgramType(StringEventType):
    """
    The name of the logic or motion program being executed by the
    {{block(Controller)}} component.
    """


@dataclass
class ResistanceType(CommonSampleType):
    """
    The measurement of the degree to which a substance opposes the passage of an
    electric current.
    """


@dataclass
class RotaryMode(RotaryModeType):
    """
    The current operating mode for a {{block(Rotary)}} type axis.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class RotaryVelocityOverrideType(FloatEventType):
    """The value of a command issued to adjust the programmed velocity for a
    {{block(Rotary)}} type axis.

    This command represents a percentage change to the velocity
    calculated by a logic or motion program or set by a switch for a
    {{block(Rotary)}} type axis.
    """


@dataclass
class RotaryVelocityType(CommonSampleType):
    """
    The measurement of the rotational speed of a rotary axis.
    """


@dataclass
class RotationType(StringEventType):
    """
    A three space angular rotation relative to a coordinate system.
    """


@dataclass
class SensorAttachmentType(StringEventType):
    """
    The reference version of the MTConnect Standard supported by the
    {{term(Adapter)}} .
    """


@dataclass
class SerialNumberType(StringEventType):
    """
    The serial number associated with a {{block(Component)}}, {{block(Asset)}}, or
    {{block(Device)}}.
    """


@dataclass
class SoundLevelType(CommonSampleType):
    """
    The measurement of a sound level or sound pressure level relative to
    atmospheric pressure.
    """


@dataclass
class SpecificationLimitType(StringEventType):
    """
    A set of limits defining a range of values designating acceptable performance
    for a variable.
    """


@dataclass
class SpindleInterlock(SpindleInterlockType):
    """
    An indication of the status of the spindle for a piece of equipment when power
    has been removed and it is free to rotate.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class SpindleSpeedType(CommonSampleType):
    """**DEPRECATED** in *Version 1.2*.

    Replaced by {{block(RotaryVelocity)}}. The rotational speed of the
    rotary axis.
    """


@dataclass
class StrainType(CommonSampleType):
    """
    The measurement of the amount of deformation per unit length of an object when
    a load is applied.
    """


@dataclass
class StringEvent(StringEventType):
    """
    An unfaceted string event.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class StringListEvent(StringListEventType):
    """
    An unfaceted string event.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class TemperatureType(CommonSampleType):
    """
    The measurement of temperature.
    """


@dataclass
class TensionType(CommonSampleType):
    """
    The measurement of a force that stretches or elongates an object.
    """


@dataclass
class ThreeSpaceSample(ThreeSpaceSampleType):
    """
    A sample with a three tuple floating point value.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class TiltType(CommonSampleType):
    """
    The measurement of angular displacement.
    """


@dataclass
class TimeSeriesType(AbsTimeSeriesType):
    """A {{block(DataItem)}} with `TIME_SERIES` {{property(representation)}}
    **MUST** have a {{property(category)}} of `SAMPLE`.

    A *Time Series*
    {{term(observation)}} **MUST** have a {{property(sampleCount)}}
    attribute. *Time Series* {{term(observation)}} **MUST** report multiple
    values at fixed intervals in a single {{term(observation)}}. At minimum,
    one of DataItem or {{term(observation)}} **MUST** specify the
    {{property(sampleRate)}} in Hertz (values/second); fractional rates are
    permitted. When the {{term(observation)}} and the {{block(DataItem)}}
    specify the {{property(sampleRate)}}, the {{term(observation)}}
    {{property(sampleRate)}} supersedes the {{block(DataItem)}}. The
    {{term(observation)}} **MUST** set the {{property(timestamp)}} to the
    time the last value was observed. The {{property(duration)}} **MAY**
    indicate the time interval from the first to the last value in the
    series. {{sect(Attributes of TimeSeries)}} defines additional attributes
    provided for a {{block(DataItem)}} of `category` `SAMPLE` with a
    {{property(representation)}} attribute of `TIME_SERIES`.
    """

    content: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    value: List[str] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )


@dataclass
class ToolAssetIdType(StringEventType):
    """
    The identifier of an individual tool asset.
    """


@dataclass
class ToolGroupType(StringEventType):
    """An identifier for the tool group associated with a specific tool.

    Commonly used to designate spare tools.
    """


@dataclass
class ToolIdType(StringEventType):
    """**DEPRECATED** in *Version 1.2.0*.

    See {{block(ToolAssetId)}}. The
    identifier of the tool currently in use for a given `Path`.
    """


@dataclass
class ToolNumberType(StringEventType):
    """
    The identifier assigned by the {{block(Controller)}} component to a cutting
    tool when in use by a piece of equipment.
    """


@dataclass
class ToolOffsetTable(ToolOffsetTableType):
    """
    Table of A reference to the tool offset variables applied to the active cutting
    tool associated with a {{block(Path)}} in a {{block(Controller)}} type
    component.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class ToolOffsetType(FloatEventType):
    """
    A reference to the tool offset variables applied to the active cutting tool
    associated with a {{block(Path)}} in a {{block(Controller)}} type component.
    """


@dataclass
class TorqueType(CommonSampleType):
    """
    The measurement of the turning force exerted on an object or by an object.
    """


@dataclass
class TranslationType(StringEventType):
    """
    A three space linear translation relative to a coordinate system.
    """


@dataclass
class Unavailable(UnavailableType):
    """
    The conditon can not be determined.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class UserType(StringEventType):
    """
    The identifier of the person currently responsible for operating the piece of
    equipment.
    """


@dataclass
class VariableDataSet(VariableDataSetType):
    """
    DataSet of A data value whose meaning may change over time due to changes in
    the opertion of a piece of equipment or the process being executed on that
    piece of equipment.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class VariableType(StringEventType):
    """
    A data value whose meaning may change over time due to changes in the opertion
    of a piece of equipment or the process being executed on that piece of
    equipment.
    """


@dataclass
class VelocityType(CommonSampleType):
    """
    The measurement of the rate of change of position of a {{block(Component)}}.
    """


@dataclass
class ViscosityType(CommonSampleType):
    """
    The measurement of a fluids resistance to flow.
    """


@dataclass
class VoltAmpereReactiveType(CommonSampleType):
    """
    The measurement of reactive power in an AC electrical circuit (commonly
    referred to as VAR).
    """


@dataclass
class VoltAmpereType(CommonSampleType):
    """
    The measurement of the apparent power in an electrical circuit, equal to the
    product of root-mean-square (RMS) voltage and RMS current (commonly referred to
    as VA).
    """


@dataclass
class VoltageActype(CommonSampleType):
    """
    The measurement of the electrical potential between two points in an electrical
    circuit in which the current periodically reverses direction.
    """

    class Meta:
        name = "VoltageACType"


@dataclass
class VoltageDctype(CommonSampleType):
    """
    The measurement of the electrical potential between two points in an electrical
    circuit in which the current is unidirectional.
    """

    class Meta:
        name = "VoltageDCType"


@dataclass
class VoltageType(CommonSampleType):
    """**DEPRECATED** in *Version 1.6*.

    Replaced by {{block(VoltageAC)}} and {{block(VoltageDC)}}. The
    measurement of electrical potential between two points.
    """


@dataclass
class VolumeFluidType(CommonSampleType):
    """
    The fluid volume of an object or container.
    """


@dataclass
class VolumeSpatialType(CommonSampleType):
    """
    The geometric volume of an object or container.
    """


@dataclass
class WaitState(WaitStateType):
    """
    An indication of the reason that {{block(Execution)}} is reporting a value of
    `WAIT`.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class Warning(WarningType):
    """
    {{block(Warning)}} indicates a possible unexpected situation because the value
    is unexpected or out of tolerance for the data.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class WattageType(CommonSampleType):
    """
    The measurement of power flowing through or dissipated by an electrical circuit
    or piece of equipment.
    """


@dataclass
class WireType(StringEventType):
    """
    A string like piece or filament of relatively rigid or flexible material
    provided in a variety of diameters.
    """


@dataclass
class WorkOffsetTable(WorkOffsetTableType):
    """
    Table of A reference to the offset variables for a work piece or part
    associated with a {{block(Path)}} in a {{block(Controller)}} type component.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class WorkOffsetType(FloatEventType):
    """
    A reference to the offset variables for a work piece or part associated with a
    {{block(Path)}} in a {{block(Controller)}} type component.
    """


@dataclass
class WorkholdingIdType(StringEventType):
    """
    The identifier for the current workholding or part clamp in use by a piece of
    equipment.
    """


@dataclass
class XdimensionType(CommonSampleType):
    """
    Measured dimension of an entity relative to the X direction of the referenced
    coordinate system.
    """

    class Meta:
        name = "XDimensionType"


@dataclass
class YdimensionType(CommonSampleType):
    """
    Measured dimension of an entity relative to the Y direction of the referenced
    coordinate system.
    """

    class Meta:
        name = "YDimensionType"


@dataclass
class ZdimensionType(CommonSampleType):
    """
    Measured dimension of an entity relative to the Z direction of the referenced
    coordinate system.
    """

    class Meta:
        name = "ZDimensionType"


@dataclass
class Acceleration(AccelerationType):
    """
    The measurement of the rate of change of velocity.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class AccelerationTimeSeriesType(TimeSeriesType):
    """
    Time series of The measurement of the rate of change of velocity.
    """


@dataclass
class AccumulatedTime(AccumulatedTimeType):
    """
    The measurement of accumulated time for an activity or event.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class AccumulatedTimeTimeSeriesType(TimeSeriesType):
    """
    Time series of The measurement of accumulated time for an activity or event.
    """


@dataclass
class ActiveAxes(ActiveAxesType):
    """
    The result is a space delimited list of axes names.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class AdapterSoftwareVersion(AdapterSoftwareVersionType):
    """
    The originator’s software version of the {{term(Adapter)}}.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class AdapterUri(AdapterUritype):
    """
    The {{term(URI)}} of the {{term(Adapter)}}.
    """

    class Meta:
        name = "AdapterURI"
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class Alarm(AlarmType):
    """
    **DEPRECATED:** Replaced with {{block(CONDITION)}} category data items in
    Version 1.1.0.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class AlarmLimit(AlarmLimitType):
    """
    A set of limits used to trigger warning or alarm indicators.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class Amperage(AmperageType):
    """**DEPRECATED** in *Version 1.6*.

    Replaced by {{block(AmperageAC)}} and {{block(AmperageDC)}}. The
    measurement of electrical current.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class AmperageAc(AmperageActype):
    """
    The measurement of an electrical current that reverses direction at regular
    short intervals.
    """

    class Meta:
        name = "AmperageAC"
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class AmperageActimeSeriesType(TimeSeriesType):
    """
    Time series of The measurement of an electrical current that reverses direction
    at regular short intervals.
    """

    class Meta:
        name = "AmperageACTimeSeriesType"


@dataclass
class AmperageDc(AmperageDctype):
    """
    The measurement of an electric current flowing in one direction only.
    """

    class Meta:
        name = "AmperageDC"
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class AmperageDctimeSeriesType(TimeSeriesType):
    """
    Time series of The measurement of an electric current flowing in one direction
    only.
    """

    class Meta:
        name = "AmperageDCTimeSeriesType"


@dataclass
class AmperageTimeSeriesType(TimeSeriesType):
    """Time series of **DEPRECATED** in *Version 1.6*.

    Replaced by {{block(AmperageAC)}} and {{block(AmperageDC)}}. The
    measurement of electrical current.
    """


@dataclass
class Angle(AngleType):
    """
    The measurement of angular position.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class AngleTimeSeriesType(TimeSeriesType):
    """
    Time series of The measurement of angular position.
    """


@dataclass
class AngularAcceleration(AngularAccelerationType):
    """
    The measurement rate of change of angular velocity.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class AngularAccelerationTimeSeriesType(TimeSeriesType):
    """
    Time series of The measurement rate of change of angular velocity.
    """


@dataclass
class AngularDeceleration(AngularDecelerationType):
    """
    Negative rate of change of angular velocity.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class AngularDecelerationTimeSeriesType(TimeSeriesType):
    """
    Time series of Negative rate of change of angular velocity.
    """


@dataclass
class AngularVelocity(AngularVelocityType):
    """
    The measurement of the rate of change of angular position.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class AngularVelocityTimeSeriesType(TimeSeriesType):
    """
    Time series of The measurement of the rate of change of angular position.
    """


@dataclass
class Application(ApplicationType):
    """Software or a program that is specific to the solution of an application
    problem.

    {{cite(ISO/IEC 20944-1:2013)}}
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class AssetChanged(AssetChangedType):
    """An {{term(MTConnect Asset)}} has been added or modified.

    The value **MUST** be the {{property(assetId)}} of the
    {{block(Asset)}} that has been modified.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class AssetRemoved(AssetRemovedType):
    """An {{term(MTConnect Asset)}} has been removed.

    The value **MUST** be the {{property(assetId)}} of the
    {{block(Asset)}} that has been removed.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class AssetUpdateRate(AssetUpdateRateType):
    """The average rate of change of values for assets in the MTConnect streams.

    The average is computed over a rolling window defined by the
    implementation.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class AssetUpdateRateTimeSeriesType(TimeSeriesType):
    """Time series of The average rate of change of values for assets in the
    MTConnect streams.

    The average is computed over a rolling window defined by the
    implementation.
    """


@dataclass
class AxisFeedrate(AxisFeedrateType):
    """
    The measurement of the feedrate of a linear axis.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class AxisFeedrateOverride(AxisFeedrateOverrideType):
    """
    The value of a signal or calculation issued to adjust the feedrate of an
    individual linear type axis.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class AxisFeedrateTimeSeriesType(TimeSeriesType):
    """
    Time series of The measurement of the feedrate of a linear axis.
    """


@dataclass
class Block(BlockType):
    """
    The line of code or command being executed by a {{block(Controller)}}
    {{term(Structural Element)}}.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class BlockCount(BlockCountType):
    """
    The total count of the number of blocks of program code that have been executed
    since execution started.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class BlockDiscreteType(BlockType):
    """
    Discrete of The line of code or command being executed by a
    {{block(Controller)}} {{term(Structural Element)}}.
    """


@dataclass
class CapacityFluid(CapacityFluidType):
    """
    The fluid capacity of an object or container.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class CapacityFluidTimeSeriesType(TimeSeriesType):
    """
    Time series of The fluid capacity of an object or container.
    """


@dataclass
class CapacitySpatial(CapacitySpatialType):
    """
    The geometric capacity of an object or container.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class CapacitySpatialTimeSeriesType(TimeSeriesType):
    """
    Time series of The geometric capacity of an object or container.
    """


@dataclass
class ClockTime(ClockTimeType):
    """
    The value provided by a timing device at a specific point in time.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class ClockTimeTimeSeriesType(TimeSeriesType):
    """
    Time series of The value provided by a timing device at a specific point in
    time.
    """


@dataclass
class CloseChuck(CloseChuckType):
    """
    Service to close a chuck.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class CloseDoor(CloseDoorType):
    """
    Service to close a door.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class Code(CodeType):
    """**DEPRECATED** in *Version 1.1*.

    The programmatic code being executed.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class CompositionState(CompositionStateType):
    """
    An indication of the operating condition of a mechanism represented by a
    {{block(Composition)}} type element.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class Concentration(ConcentrationType):
    """
    The measurement of the percentage of one component within a mixture of
    components.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class ConcentrationTimeSeriesType(TimeSeriesType):
    """
    Time series of The measurement of the percentage of one component within a
    mixture of components.
    """


@dataclass
class ConditionListType:
    """
    A collection of conditions.
    """

    fault: List[Fault] = field(
        default_factory=list,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    warning: List[Warning] = field(
        default_factory=list,
        metadata={
            "name": "Warning",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    normal: List[Normal] = field(
        default_factory=list,
        metadata={
            "name": "Normal",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    unavailable: List[Unavailable] = field(
        default_factory=list,
        metadata={
            "name": "Unavailable",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )


@dataclass
class Conductivity(ConductivityType):
    """
    The measurement of the ability of a material to conduct electricity.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class ConductivityTimeSeriesType(TimeSeriesType):
    """
    Time series of The measurement of the ability of a material to conduct
    electricity.
    """


@dataclass
class ControlLimit(ControlLimitType):
    """
    A set of limits used to indicate whether a process variable is stable and in
    control.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class CoupledAxes(CoupledAxesType):
    """
    Refers to the set of associated axes.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class CuttingSpeed(CuttingSpeedType):
    """
    The speed difference (relative velocity) between the cutting mechanism and the
    surface of the workpiece it is operating on.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class CuttingSpeedTimeSeriesType(TimeSeriesType):
    """
    Time series of The speed difference (relative velocity) between the cutting
    mechanism and the surface of the workpiece it is operating on.
    """


@dataclass
class DateCode(DateCodeType):
    """The time and date code associated with a material or other physical item.

    {{block(DATE_CODE)}} **MUST** be reported in ISO 8601 format.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class Deceleration(DecelerationType):
    """
    Negative rate of change of velocity.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class DecelerationTimeSeriesType(TimeSeriesType):
    """
    Time series of Negative rate of change of velocity.
    """


@dataclass
class Density(DensityType):
    """
    The volumetric mass of a material per unit volume of that material.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class DensityTimeSeriesType(TimeSeriesType):
    """
    Time series of The volumetric mass of a material per unit volume of that
    material.
    """


@dataclass
class DepositionAccelerationVolumetric(DepositionAccelerationVolumetricType):
    """
    The rate of change in spatial volume of material deposited in an additive
    manufacturing process.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class DepositionAccelerationVolumetricTimeSeriesType(TimeSeriesType):
    """
    Time series of The rate of change in spatial volume of material deposited in an
    additive manufacturing process.
    """


@dataclass
class DepositionDensity(DepositionDensityType):
    """
    The density of the material deposited in an additive manufacturing process per
    unit of volume.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class DepositionDensityTimeSeriesType(TimeSeriesType):
    """
    Time series of The density of the material deposited in an additive
    manufacturing process per unit of volume.
    """


@dataclass
class DepositionMass(DepositionMassType):
    """
    The mass of the material deposited in an additive manufacturing process.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class DepositionMassTimeSeriesType(TimeSeriesType):
    """
    Time series of The mass of the material deposited in an additive manufacturing
    process.
    """


@dataclass
class DepositionRateVolumetric(DepositionRateVolumetricType):
    """
    The rate at which a spatial volume of material is deposited in an additive
    manufacturing process.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class DepositionRateVolumetricTimeSeriesType(TimeSeriesType):
    """
    Time series of The rate at which a spatial volume of material is deposited in
    an additive manufacturing process.
    """


@dataclass
class DepositionVolume(DepositionVolumeType):
    """
    The spatial volume of material to be deposited in an additive manufacturing
    process.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class DepositionVolumeTimeSeriesType(TimeSeriesType):
    """
    Time series of The spatial volume of material to be deposited in an additive
    manufacturing process.
    """


@dataclass
class DeviceAdded(DeviceAddedType):
    """
    An {{block(Event)}} that provides the {{term(UUID)}} of new device added to an
    {{term(MTConnect Agent)}}.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class DeviceChanged(DeviceChangedType):
    """
    An {{block(Event)}} that provides the {{term(UUID)}} of the device whose
    {{term(Metadata)}} has changed.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class DeviceRemoved(DeviceRemovedType):
    """
    An {{block(Event)}} that provides the {{term(UUID)}} of a device removed from
    an {{term(MTConnect Agent)}}.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class DeviceUuid(DeviceUuidType):
    """
    The identifier of another piece of equipment that is temporarily associated
    with a component of this piece of equipment to perform a particular function.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class Diameter(DiameterType):
    """
    The measured dimension of a diameter.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class DiameterTimeSeriesType(TimeSeriesType):
    """
    Time series of The measured dimension of a diameter.
    """


@dataclass
class Direction(DirectionType):
    """
    An indication of a fault associated with the direction of motion of a
    {{term(Structural Element)}}.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class Displacement(DisplacementType):
    """
    The measurement of the change in position of an object.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class DisplacementTimeSeriesType(TimeSeriesType):
    """
    Time series of The measurement of the change in position of an object.
    """


@dataclass
class ElectricalEnergy(ElectricalEnergyType):
    """
    The measurement of electrical energy consumption by a component.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class ElectricalEnergyTimeSeriesType(TimeSeriesType):
    """
    Time series of The measurement of electrical energy consumption by a component.
    """


@dataclass
class EquipmentTimer(EquipmentTimerType):
    """
    The measurement of the amount of time a piece of equipment or a sub-part of a
    piece of equipment has performed specific activities.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class EquipmentTimerTimeSeriesType(TimeSeriesType):
    """
    Time series of The measurement of the amount of time a piece of equipment or a
    sub-part of a piece of equipment has performed specific activities.
    """


@dataclass
class FillLevel(FillLevelType):
    """
    The measurement of the amount of a substance remaining compared to the planned
    maximum amount of that substance.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class FillLevelTimeSeriesType(TimeSeriesType):
    """
    Time series of The measurement of the amount of a substance remaining compared
    to the planned maximum amount of that substance.
    """


@dataclass
class Firmware(FirmwareType):
    """
    The embedded software of a component.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class Flow(FlowType):
    """
    The measurement of the rate of flow of a fluid.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class FlowTimeSeriesType(TimeSeriesType):
    """
    Time series of The measurement of the rate of flow of a fluid.
    """


@dataclass
class Frequency(FrequencyType):
    """
    The measurement of the number of occurrences of a repeating event per unit
    time.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class FrequencyTimeSeriesType(TimeSeriesType):
    """
    Time series of The measurement of the number of occurrences of a repeating
    event per unit time.
    """


@dataclass
class GlobalPosition(GlobalPositionType):
    """
    **DEPRECATED** in Version 1.1.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class GlobalPositionTimeSeriesType(TimeSeriesType):
    """
    Time series of **DEPRECATED** in Version 1.1.
    """


@dataclass
class Hardness(HardnessType):
    """
    The measurement of the hardness of a material.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class Hardware(HardwareType):
    """
    An indication of a fault associated with the hardware subsystem of the
    {{term(Structural Element)}}.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class HumidityAbsolute(HumidityAbsoluteType):
    """
    The amount of water vapor expressed in grams per cubic meter.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class HumidityAbsoluteTimeSeriesType(TimeSeriesType):
    """
    Time series of The amount of water vapor expressed in grams per cubic meter.
    """


@dataclass
class HumidityRelative(HumidityRelativeType):
    """
    The amount of water vapor present expressed as a percent to reach saturation at
    the same temperature.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class HumidityRelativeTimeSeriesType(TimeSeriesType):
    """
    Time series of The amount of water vapor present expressed as a percent to
    reach saturation at the same temperature.
    """


@dataclass
class HumiditySpecific(HumiditySpecificType):
    """
    The ratio of the water vapor present over the total weight of the water vapor
    and air present expressed as a percent.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class HumiditySpecificTimeSeriesType(TimeSeriesType):
    """
    Time series of The ratio of the water vapor present over the total weight of
    the water vapor and air present expressed as a percent.
    """


@dataclass
class Length(LengthType):
    """
    The measurement of the length of an object.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class LengthTimeSeriesType(TimeSeriesType):
    """
    Time series of The measurement of the length of an object.
    """


@dataclass
class Level(LevelType):
    """**DEPRECATED** in *Version 1.2*.

    See {{block(FillLevel)}}. Represents the level of a resource.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class LevelTimeSeriesType(TimeSeriesType):
    """Time series of **DEPRECATED** in *Version 1.2*.

    See {{block(FillLevel)}}. Represents the level of a resource.
    """


@dataclass
class Library(LibraryType):
    """
    The software library on a component.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class Line(LineType):
    """**DEPRECATED** in *Version 1.4.0*.

    The current line of code being executed.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class LineLabel(LineLabelType):
    """
    An optional identifier for a {{block(Block)}} of code in a {{block(Program)}}.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class LineNumber(LineNumberType):
    """
    A reference to the position of a block of program code within a control
    program.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class LinearForce(LinearForceType):
    """
    The measurement of the push or pull introduced by an actuator or exerted on an
    object.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class LinearForceTimeSeriesType(TimeSeriesType):
    """
    Time series of The measurement of the push or pull introduced by an actuator or
    exerted on an object.
    """


@dataclass
class Load(LoadType):
    """
    The measurement of the actual versus the standard rating of a piece of
    equipment.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class LoadTimeSeriesType(TimeSeriesType):
    """
    Time series of The measurement of the actual versus the standard rating of a
    piece of equipment.
    """


@dataclass
class MtconnectVersion(MtconnectVersionType):
    """
    The reference version of the MTConnect Standard supported by the
    {{term(Adapter)}} .
    """

    class Meta:
        name = "MTConnectVersion"
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class Mass(MassType):
    """
    The measurement of the mass of an object(s) or an amount of material.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class MassTimeSeriesType(TimeSeriesType):
    """
    Time series of The measurement of the mass of an object(s) or an amount of
    material.
    """


@dataclass
class Material(MaterialType):
    """
    {{block(Materials)}} provides information about materials or other items
    consumed or used by the piece of equipment for production of parts, materials,
    or other types of goods.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class MaterialChange(MaterialChangeType):
    """
    Service to change the type of material or product being loaded or fed to a
    piece of equipment.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class MaterialFeed(MaterialFeedType):
    """
    Service to advance material or feed product to a piece of equipment from a
    continuous or bulk source.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class MaterialLayer(MaterialLayerType):
    """
    Identifies the layers of material applied to a part or product as part of an
    additive manufacturing process.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class MaterialLoad(MaterialLoadType):
    """
    Service to load a piece of material or product.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class MaterialRetract(MaterialRetractType):
    """
    Service to remove or retract material or product.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class MaterialUnload(MaterialUnloadType):
    """
    Service to unload a piece of material or product.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class Message(MessageType):
    """
    A communication in writing, in speech, or by signals.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class MessageDiscreteType(MessageType):
    """
    Discrete of A communication in writing, in speech, or by signals.
    """


@dataclass
class Network(NetworkType):
    """
    Network details of a component.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class ObservationUpdateRate(ObservationUpdateRateType):
    """The average rate of change of values for data items in the MTConnect
    streams.

    The average is computed over a rolling window defined by the
    implementation.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class ObservationUpdateRateTimeSeriesType(TimeSeriesType):
    """Time series of The average rate of change of values for data items in the
    MTConnect streams.

    The average is computed over a rolling window defined by the
    implementation.
    """


@dataclass
class OpenChuck(OpenChuckType):
    """
    Service to open a chuck.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class OpenDoor(OpenDoorType):
    """
    Service to open a door.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class OperatingSystem(OperatingSystemType):
    """
    The Operating System of a component.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class OperatorId(OperatorIdType):
    """
    The identifier of the person currently responsible for operating the piece of
    equipment.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class Orientation(OrientationType):
    """
    A measured or calculated orientation of a plane or vector relative to a
    cartesian coordinate system.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class Ph(Phtype):
    """
    A measure of the acidity or alkalinity of a solution.
    """

    class Meta:
        name = "PH"
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class PhtimeSeriesType(TimeSeriesType):
    """
    Time series of A measure of the acidity or alkalinity of a solution.
    """

    class Meta:
        name = "PHTimeSeriesType"


@dataclass
class PalletId(PalletIdType):
    """
    The identifier for a pallet.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class PalletIdDiscreteType(PalletIdType):
    """
    Discrete of The identifier for a pallet.
    """


@dataclass
class PartChange(PartChangeType):
    """
    Service to change the part or product associated with a piece of equipment to a
    different part or product.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class PartCount(PartCountType):
    """
    The aggregate count of parts.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class PartCountDiscreteType(PartCountType):
    """
    Discrete of The aggregate count of parts.
    """


@dataclass
class PartGroupId(PartGroupIdType):
    """Identifier given to a collection of individual parts.

    If no
    {{property(subType)}} is specified, `UUID` is default.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class PartId(PartIdType):
    """
    An identifier of a part in a manufacturing operation.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class PartKindId(PartKindIdType):
    """Identifier given to link the individual occurrence to a class of parts,
    typically distinguished by a particular part design.

    If no
    {{property(subType)}} is specified, `UUID` is default.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class PartNumber(PartNumberType):
    """**DEPRECATED** in *Version 1.7*.

    {{block(PartNumber)}} is now a
    `subType` of {{block(PartKindId)}}. An identifier of a part or product
    moving through the manufacturing process.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class PartUniqueId(PartUniqueIdType):
    """Identifier given to a distinguishable, individual part.

    If no
    {{property(subType)}} is specified, `UUID` is default.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class PathFeedrate(PathFeedrateType):
    """
    The measurement of the feedrate for the axes, or a single axis, associated with
    a {{block(Path)}} component-a vector.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class PathFeedrateOverride(PathFeedrateOverrideType):
    """
    The value of a signal or calculation issued to adjust the feedrate for the axes
    associated with a {{block(Path)}} component that may represent a single axis or
    the coordinated movement of multiple axes.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class PathFeedratePerRevolution(PathFeedratePerRevolutionType):
    """
    The feedrate for the axes, or a single axis.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class PathFeedratePerRevolutionTimeSeriesType(TimeSeriesType):
    """
    Time series of The feedrate for the axes, or a single axis.
    """


@dataclass
class PathFeedrateTimeSeriesType(TimeSeriesType):
    """
    Time series of The measurement of the feedrate for the axes, or a single axis,
    associated with a {{block(Path)}} component-a vector.
    """


@dataclass
class PathPosition(PathPositionType):
    """
    A measured or calculated position of a control point associated with a
    {{block(Controller)}} element, or {{block(Path)}} element if provided, of a
    piece of equipment.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class Position(PositionType):
    """
    A measured or calculated position of a {{block(Component)}} element as reported
    by a piece of equipment.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class PositionTimeSeriesType(TimeSeriesType):
    """
    Time series of A measured or calculated position of a {{block(Component)}}
    element as reported by a piece of equipment.
    """


@dataclass
class PowerFactor(PowerFactorType):
    """
    The measurement of the ratio of real power flowing to a load to the apparent
    power in that AC circuit.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class PowerFactorTimeSeriesType(TimeSeriesType):
    """
    Time series of The measurement of the ratio of real power flowing to a load to
    the apparent power in that AC circuit.
    """


@dataclass
class PowerStatus(PowerStatusType):
    """**DEPRECATED** in *Version 1.1.0*.

    The `ON` or `OFF` status of the
    component.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class Pressure(PressureType):
    """{{block(Pressure)}} is a system that delivers compressed gas or fluid and
    controls the pressure and rate of pressure change to a desired target set-
    point.

    Note: For example, Delivery Method can be a Compressed
    Air or N2 tank that is piped via an inlet valve to the chamber.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class PressureAbsolute(PressureAbsoluteType):
    """
    The force per unit area measured relative to a vacuum.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class PressureAbsoluteTimeSeriesType(TimeSeriesType):
    """
    Time series of The force per unit area measured relative to a vacuum.
    """


@dataclass
class PressureTimeSeriesType(TimeSeriesType):
    """Time series of The force per unit area measured relative to atmospheric
    pressure.

    Commonly referred to as gauge pressure.
    """


@dataclass
class PressurizationRate(PressurizationRateType):
    """
    The change of pressure per unit time.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class PressurizationRateTimeSeriesType(TimeSeriesType):
    """
    Time series of The change of pressure per unit time.
    """


@dataclass
class ProcessAggregateId(ProcessAggregateIdType):
    """
    Identifier given to link the individual occurrence to a group of related
    occurrences, such as a process step in a process plan.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class ProcessKindId(ProcessKindIdType):
    """
    Identifier given to link the individual occurrence to a class of processes or
    process definition.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class ProcessOccurrenceId(ProcessOccurrenceIdType):
    """
    An identifier of a process being executed by the device.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class ProcessTime(ProcessTimeType):
    """The time and date associated with an activity or event.

    {{block(ProcessTime)}} **MUST** be reported in ISO 8601 format.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class ProcessTimer(ProcessTimerType):
    """
    The measurement of the amount of time a piece of equipment has performed
    different types of activities associated with the process being performed at
    that piece of equipment.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class ProcessTimerTimeSeriesType(TimeSeriesType):
    """
    Time series of The measurement of the amount of time a piece of equipment has
    performed different types of activities associated with the process being
    performed at that piece of equipment.
    """


@dataclass
class Program(ProgramType):
    """
    The name of the logic or motion program being executed by the
    {{block(Controller)}} component.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class ProgramComment(ProgramCommentType):
    """
    A comment or non-executable statement in the control program.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class ProgramEditName(ProgramEditNameType):
    """The name of the program being edited.

    This is used in conjunction with
    {{block(ProgramEdit)}} when in `ACTIVE` state.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class ProgramHeader(ProgramHeaderType):
    """
    The non-executable header section of the control program.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class ProgramLocation(ProgramLocationType1):
    """
    The Uniform Resource Identifier (URI) for the source file associated with
    {{block(Program)}}.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class ProgramLocationType(ProgramLocationTypeType):
    """
    Defines whether the logic or motion program defined by {{block(Program)}} is
    being executed from the local memory of the controller or from an outside
    source.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class ProgramNestLevel(ProgramNestLevelType):
    """An indication of the nesting level within a control program that is
    associated with the code or instructions that is currently being executed.

    If an Initial Value is not defined, the nesting level associated
    with the highest or initial nesting level of the program **MUST**
    default to zero (0).
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class Resistance(ResistanceType):
    """
    The measurement of the degree to which a substance opposes the passage of an
    electric current.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class ResistanceTimeSeriesType(TimeSeriesType):
    """
    Time series of The measurement of the degree to which a substance opposes the
    passage of an electric current.
    """


@dataclass
class RotaryVelocity(RotaryVelocityType):
    """
    The measurement of the rotational speed of a rotary axis.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class RotaryVelocityOverride(RotaryVelocityOverrideType):
    """The value of a command issued to adjust the programmed velocity for a
    {{block(Rotary)}} type axis.

    This command represents a percentage change to the velocity
    calculated by a logic or motion program or set by a switch for a
    {{block(Rotary)}} type axis.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class RotaryVelocityTimeSeriesType(TimeSeriesType):
    """
    Time series of The measurement of the rotational speed of a rotary axis.
    """


@dataclass
class Rotation(RotationType):
    """
    A three space angular rotation relative to a coordinate system.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class SensorAttachment(SensorAttachmentType):
    """
    The reference version of the MTConnect Standard supported by the
    {{term(Adapter)}} .
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class SerialNumber(SerialNumberType):
    """
    The serial number associated with a {{block(Component)}}, {{block(Asset)}}, or
    {{block(Device)}}.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class SoundLevel(SoundLevelType):
    """
    The measurement of a sound level or sound pressure level relative to
    atmospheric pressure.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class SoundLevelTimeSeriesType(TimeSeriesType):
    """
    Time series of The measurement of a sound level or sound pressure level
    relative to atmospheric pressure.
    """


@dataclass
class SpecificationLimit(SpecificationLimitType):
    """
    A set of limits defining a range of values designating acceptable performance
    for a variable.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class SpindleSpeed(SpindleSpeedType):
    """**DEPRECATED** in *Version 1.2*.

    Replaced by {{block(RotaryVelocity)}}. The rotational speed of the
    rotary axis.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class SpindleSpeedTimeSeriesType(TimeSeriesType):
    """Time series of **DEPRECATED** in *Version 1.2*.

    Replaced by {{block(RotaryVelocity)}}. The rotational speed of the
    rotary axis.
    """


@dataclass
class Strain(StrainType):
    """
    The measurement of the amount of deformation per unit length of an object when
    a load is applied.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class StrainTimeSeriesType(TimeSeriesType):
    """
    Time series of The measurement of the amount of deformation per unit length of
    an object when a load is applied.
    """


@dataclass
class Temperature(TemperatureType):
    """
    The measurement of temperature.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class TemperatureTimeSeriesType(TimeSeriesType):
    """
    Time series of The measurement of temperature.
    """


@dataclass
class Tension(TensionType):
    """
    The measurement of a force that stretches or elongates an object.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class TensionTimeSeriesType(TimeSeriesType):
    """
    Time series of The measurement of a force that stretches or elongates an
    object.
    """


@dataclass
class Tilt(TiltType):
    """
    The measurement of angular displacement.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class TiltTimeSeriesType(TimeSeriesType):
    """
    Time series of The measurement of angular displacement.
    """


@dataclass
class TimeSeries(TimeSeriesType):
    """A {{block(DataItem)}} with `TIME_SERIES` {{property(representation)}}
    **MUST** have a {{property(category)}} of `SAMPLE`.

    A *Time Series*
    {{term(observation)}} **MUST** have a {{property(sampleCount)}}
    attribute. *Time Series* {{term(observation)}} **MUST** report multiple
    values at fixed intervals in a single {{term(observation)}}. At minimum,
    one of DataItem or {{term(observation)}} **MUST** specify the
    {{property(sampleRate)}} in Hertz (values/second); fractional rates are
    permitted. When the {{term(observation)}} and the {{block(DataItem)}}
    specify the {{property(sampleRate)}}, the {{term(observation)}}
    {{property(sampleRate)}} supersedes the {{block(DataItem)}}. The
    {{term(observation)}} **MUST** set the {{property(timestamp)}} to the
    time the last value was observed. The {{property(duration)}} **MAY**
    indicate the time interval from the first to the last value in the
    series. {{sect(Attributes of TimeSeries)}} defines additional attributes
    provided for a {{block(DataItem)}} of `category` `SAMPLE` with a
    {{property(representation)}} attribute of `TIME_SERIES`.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class ToolAssetId(ToolAssetIdType):
    """
    The identifier of an individual tool asset.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class ToolAssetIdDiscreteType(ToolAssetIdType):
    """
    Discrete of The identifier of an individual tool asset.
    """


@dataclass
class ToolGroup(ToolGroupType):
    """An identifier for the tool group associated with a specific tool.

    Commonly used to designate spare tools.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class ToolId(ToolIdType):
    """**DEPRECATED** in *Version 1.2.0*.

    See {{block(ToolAssetId)}}. The
    identifier of the tool currently in use for a given `Path`.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class ToolIdDiscreteType(ToolIdType):
    """Discrete of **DEPRECATED** in *Version 1.2.0*.

    See
    {{block(ToolAssetId)}}. The identifier of the tool currently in use for
    a given `Path`.
    """


@dataclass
class ToolNumber(ToolNumberType):
    """
    The identifier assigned by the {{block(Controller)}} component to a cutting
    tool when in use by a piece of equipment.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class ToolNumberDiscreteType(ToolNumberType):
    """
    Discrete of The identifier assigned by the {{block(Controller)}} component to a
    cutting tool when in use by a piece of equipment.
    """


@dataclass
class ToolOffset(ToolOffsetType):
    """
    A reference to the tool offset variables applied to the active cutting tool
    associated with a {{block(Path)}} in a {{block(Controller)}} type component.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class Torque(TorqueType):
    """
    The measurement of the turning force exerted on an object or by an object.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class TorqueTimeSeriesType(TimeSeriesType):
    """
    Time series of The measurement of the turning force exerted on an object or by
    an object.
    """


@dataclass
class Translation(TranslationType):
    """
    A three space linear translation relative to a coordinate system.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class User(UserType):
    """
    The identifier of the person currently responsible for operating the piece of
    equipment.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class Variable(VariableType):
    """
    A data value whose meaning may change over time due to changes in the opertion
    of a piece of equipment or the process being executed on that piece of
    equipment.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class Velocity(VelocityType):
    """
    The measurement of the rate of change of position of a {{block(Component)}}.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class VelocityTimeSeriesType(TimeSeriesType):
    """
    Time series of The measurement of the rate of change of position of a
    {{block(Component)}}.
    """


@dataclass
class Viscosity(ViscosityType):
    """
    The measurement of a fluids resistance to flow.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class ViscosityTimeSeriesType(TimeSeriesType):
    """
    Time series of The measurement of a fluids resistance to flow.
    """


@dataclass
class VoltAmpere(VoltAmpereType):
    """
    The measurement of the apparent power in an electrical circuit, equal to the
    product of root-mean-square (RMS) voltage and RMS current (commonly referred to
    as VA).
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class VoltAmpereReactive(VoltAmpereReactiveType):
    """
    The measurement of reactive power in an AC electrical circuit (commonly
    referred to as VAR).
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class VoltAmpereReactiveTimeSeriesType(TimeSeriesType):
    """
    Time series of The measurement of reactive power in an AC electrical circuit
    (commonly referred to as VAR).
    """


@dataclass
class VoltAmpereTimeSeriesType(TimeSeriesType):
    """
    Time series of The measurement of the apparent power in an electrical circuit,
    equal to the product of root-mean-square (RMS) voltage and RMS current
    (commonly referred to as VA).
    """


@dataclass
class Voltage(VoltageType):
    """**DEPRECATED** in *Version 1.6*.

    Replaced by {{block(VoltageAC)}} and {{block(VoltageDC)}}. The
    measurement of electrical potential between two points.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class VoltageAc(VoltageActype):
    """
    The measurement of the electrical potential between two points in an electrical
    circuit in which the current periodically reverses direction.
    """

    class Meta:
        name = "VoltageAC"
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class VoltageActimeSeriesType(TimeSeriesType):
    """
    Time series of The measurement of the electrical potential between two points
    in an electrical circuit in which the current periodically reverses direction.
    """

    class Meta:
        name = "VoltageACTimeSeriesType"


@dataclass
class VoltageDc(VoltageDctype):
    """
    The measurement of the electrical potential between two points in an electrical
    circuit in which the current is unidirectional.
    """

    class Meta:
        name = "VoltageDC"
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class VoltageDctimeSeriesType(TimeSeriesType):
    """
    Time series of The measurement of the electrical potential between two points
    in an electrical circuit in which the current is unidirectional.
    """

    class Meta:
        name = "VoltageDCTimeSeriesType"


@dataclass
class VoltageTimeSeriesType(TimeSeriesType):
    """Time series of **DEPRECATED** in *Version 1.6*.

    Replaced by {{block(VoltageAC)}} and {{block(VoltageDC)}}. The
    measurement of electrical potential between two points.
    """


@dataclass
class VolumeFluid(VolumeFluidType):
    """
    The fluid volume of an object or container.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class VolumeFluidTimeSeriesType(TimeSeriesType):
    """
    Time series of The fluid volume of an object or container.
    """


@dataclass
class VolumeSpatial(VolumeSpatialType):
    """
    The geometric volume of an object or container.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class VolumeSpatialTimeSeriesType(TimeSeriesType):
    """
    Time series of The geometric volume of an object or container.
    """


@dataclass
class Wattage(WattageType):
    """
    The measurement of power flowing through or dissipated by an electrical circuit
    or piece of equipment.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class WattageTimeSeriesType(TimeSeriesType):
    """
    Time series of The measurement of power flowing through or dissipated by an
    electrical circuit or piece of equipment.
    """


@dataclass
class Wire(WireType):
    """
    A string like piece or filament of relatively rigid or flexible material
    provided in a variety of diameters.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class WorkOffset(WorkOffsetType):
    """
    A reference to the offset variables for a work piece or part associated with a
    {{block(Path)}} in a {{block(Controller)}} type component.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class WorkholdingId(WorkholdingIdType):
    """
    The identifier for the current workholding or part clamp in use by a piece of
    equipment.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class Xdimension(XdimensionType):
    """
    Measured dimension of an entity relative to the X direction of the referenced
    coordinate system.
    """

    class Meta:
        name = "XDimension"
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class XdimensionTimeSeriesType(TimeSeriesType):
    """
    Time series of Measured dimension of an entity relative to the X direction of
    the referenced coordinate system.
    """

    class Meta:
        name = "XDimensionTimeSeriesType"


@dataclass
class Ydimension(YdimensionType):
    """
    Measured dimension of an entity relative to the Y direction of the referenced
    coordinate system.
    """

    class Meta:
        name = "YDimension"
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class YdimensionTimeSeriesType(TimeSeriesType):
    """
    Time series of Measured dimension of an entity relative to the Y direction of
    the referenced coordinate system.
    """

    class Meta:
        name = "YDimensionTimeSeriesType"


@dataclass
class Zdimension(ZdimensionType):
    """
    Measured dimension of an entity relative to the Z direction of the referenced
    coordinate system.
    """

    class Meta:
        name = "ZDimension"
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class ZdimensionTimeSeriesType(TimeSeriesType):
    """
    Time series of Measured dimension of an entity relative to the Z direction of
    the referenced coordinate system.
    """

    class Meta:
        name = "ZDimensionTimeSeriesType"


@dataclass
class AccelerationTimeSeries(AccelerationTimeSeriesType):
    """
    Time series of The measurement of the rate of change of velocity.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class AccumulatedTimeTimeSeries(AccumulatedTimeTimeSeriesType):
    """
    Time series of The measurement of accumulated time for an activity or event.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class AmperageActimeSeries(AmperageActimeSeriesType):
    """
    Time series of The measurement of an electrical current that reverses direction
    at regular short intervals.
    """

    class Meta:
        name = "AmperageACTimeSeries"
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class AmperageDctimeSeries(AmperageDctimeSeriesType):
    """
    Time series of The measurement of an electric current flowing in one direction
    only.
    """

    class Meta:
        name = "AmperageDCTimeSeries"
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class AmperageTimeSeries(AmperageTimeSeriesType):
    """Time series of **DEPRECATED** in *Version 1.6*.

    Replaced by {{block(AmperageAC)}} and {{block(AmperageDC)}}. The
    measurement of electrical current.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class AngleTimeSeries(AngleTimeSeriesType):
    """
    Time series of The measurement of angular position.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class AngularAccelerationTimeSeries(AngularAccelerationTimeSeriesType):
    """
    Time series of The measurement rate of change of angular velocity.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class AngularDecelerationTimeSeries(AngularDecelerationTimeSeriesType):
    """
    Time series of Negative rate of change of angular velocity.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class AngularVelocityTimeSeries(AngularVelocityTimeSeriesType):
    """
    Time series of The measurement of the rate of change of angular position.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class AssetUpdateRateTimeSeries(AssetUpdateRateTimeSeriesType):
    """Time series of The average rate of change of values for assets in the
    MTConnect streams.

    The average is computed over a rolling window defined by the
    implementation.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class AxisFeedrateTimeSeries(AxisFeedrateTimeSeriesType):
    """
    Time series of The measurement of the feedrate of a linear axis.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class BlockDiscrete(BlockDiscreteType):
    """
    Discrete of The line of code or command being executed by a
    {{block(Controller)}} {{term(Structural Element)}}.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class CapacityFluidTimeSeries(CapacityFluidTimeSeriesType):
    """
    Time series of The fluid capacity of an object or container.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class CapacitySpatialTimeSeries(CapacitySpatialTimeSeriesType):
    """
    Time series of The geometric capacity of an object or container.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class ClockTimeTimeSeries(ClockTimeTimeSeriesType):
    """
    Time series of The value provided by a timing device at a specific point in
    time.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class ConcentrationTimeSeries(ConcentrationTimeSeriesType):
    """
    Time series of The measurement of the percentage of one component within a
    mixture of components.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class ConductivityTimeSeries(ConductivityTimeSeriesType):
    """
    Time series of The measurement of the ability of a material to conduct
    electricity.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class CuttingSpeedTimeSeries(CuttingSpeedTimeSeriesType):
    """
    Time series of The speed difference (relative velocity) between the cutting
    mechanism and the surface of the workpiece it is operating on.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class DecelerationTimeSeries(DecelerationTimeSeriesType):
    """
    Time series of Negative rate of change of velocity.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class DensityTimeSeries(DensityTimeSeriesType):
    """
    Time series of The volumetric mass of a material per unit volume of that
    material.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class DepositionAccelerationVolumetricTimeSeries(
    DepositionAccelerationVolumetricTimeSeriesType
):
    """
    Time series of The rate of change in spatial volume of material deposited in an
    additive manufacturing process.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class DepositionDensityTimeSeries(DepositionDensityTimeSeriesType):
    """
    Time series of The density of the material deposited in an additive
    manufacturing process per unit of volume.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class DepositionMassTimeSeries(DepositionMassTimeSeriesType):
    """
    Time series of The mass of the material deposited in an additive manufacturing
    process.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class DepositionRateVolumetricTimeSeries(
    DepositionRateVolumetricTimeSeriesType
):
    """
    Time series of The rate at which a spatial volume of material is deposited in
    an additive manufacturing process.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class DepositionVolumeTimeSeries(DepositionVolumeTimeSeriesType):
    """
    Time series of The spatial volume of material to be deposited in an additive
    manufacturing process.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class DiameterTimeSeries(DiameterTimeSeriesType):
    """
    Time series of The measured dimension of a diameter.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class DisplacementTimeSeries(DisplacementTimeSeriesType):
    """
    Time series of The measurement of the change in position of an object.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class ElectricalEnergyTimeSeries(ElectricalEnergyTimeSeriesType):
    """
    Time series of The measurement of electrical energy consumption by a component.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class EquipmentTimerTimeSeries(EquipmentTimerTimeSeriesType):
    """
    Time series of The measurement of the amount of time a piece of equipment or a
    sub-part of a piece of equipment has performed specific activities.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class FillLevelTimeSeries(FillLevelTimeSeriesType):
    """
    Time series of The measurement of the amount of a substance remaining compared
    to the planned maximum amount of that substance.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class FlowTimeSeries(FlowTimeSeriesType):
    """
    Time series of The measurement of the rate of flow of a fluid.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class FrequencyTimeSeries(FrequencyTimeSeriesType):
    """
    Time series of The measurement of the number of occurrences of a repeating
    event per unit time.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class GlobalPositionTimeSeries(GlobalPositionTimeSeriesType):
    """
    Time series of **DEPRECATED** in Version 1.1.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class HumidityAbsoluteTimeSeries(HumidityAbsoluteTimeSeriesType):
    """
    Time series of The amount of water vapor expressed in grams per cubic meter.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class HumidityRelativeTimeSeries(HumidityRelativeTimeSeriesType):
    """
    Time series of The amount of water vapor present expressed as a percent to
    reach saturation at the same temperature.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class HumiditySpecificTimeSeries(HumiditySpecificTimeSeriesType):
    """
    Time series of The ratio of the water vapor present over the total weight of
    the water vapor and air present expressed as a percent.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class LengthTimeSeries(LengthTimeSeriesType):
    """
    Time series of The measurement of the length of an object.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class LevelTimeSeries(LevelTimeSeriesType):
    """Time series of **DEPRECATED** in *Version 1.2*.

    See {{block(FillLevel)}}. Represents the level of a resource.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class LinearForceTimeSeries(LinearForceTimeSeriesType):
    """
    Time series of The measurement of the push or pull introduced by an actuator or
    exerted on an object.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class LoadTimeSeries(LoadTimeSeriesType):
    """
    Time series of The measurement of the actual versus the standard rating of a
    piece of equipment.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class MassTimeSeries(MassTimeSeriesType):
    """
    Time series of The measurement of the mass of an object(s) or an amount of
    material.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class MessageDiscrete(MessageDiscreteType):
    """
    Discrete of A communication in writing, in speech, or by signals.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class ObservationUpdateRateTimeSeries(ObservationUpdateRateTimeSeriesType):
    """Time series of The average rate of change of values for data items in the
    MTConnect streams.

    The average is computed over a rolling window defined by the
    implementation.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class PhtimeSeries(PhtimeSeriesType):
    """
    Time series of A measure of the acidity or alkalinity of a solution.
    """

    class Meta:
        name = "PHTimeSeries"
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class PalletIdDiscrete(PalletIdDiscreteType):
    """
    Discrete of The identifier for a pallet.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class PartCountDiscrete(PartCountDiscreteType):
    """
    Discrete of The aggregate count of parts.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class PathFeedratePerRevolutionTimeSeries(
    PathFeedratePerRevolutionTimeSeriesType
):
    """
    Time series of The feedrate for the axes, or a single axis.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class PathFeedrateTimeSeries(PathFeedrateTimeSeriesType):
    """
    Time series of The measurement of the feedrate for the axes, or a single axis,
    associated with a {{block(Path)}} component-a vector.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class PositionTimeSeries(PositionTimeSeriesType):
    """
    Time series of A measured or calculated position of a {{block(Component)}}
    element as reported by a piece of equipment.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class PowerFactorTimeSeries(PowerFactorTimeSeriesType):
    """
    Time series of The measurement of the ratio of real power flowing to a load to
    the apparent power in that AC circuit.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class PressureAbsoluteTimeSeries(PressureAbsoluteTimeSeriesType):
    """
    Time series of The force per unit area measured relative to a vacuum.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class PressureTimeSeries(PressureTimeSeriesType):
    """Time series of The force per unit area measured relative to atmospheric
    pressure.

    Commonly referred to as gauge pressure.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class PressurizationRateTimeSeries(PressurizationRateTimeSeriesType):
    """
    Time series of The change of pressure per unit time.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class ProcessTimerTimeSeries(ProcessTimerTimeSeriesType):
    """
    Time series of The measurement of the amount of time a piece of equipment has
    performed different types of activities associated with the process being
    performed at that piece of equipment.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class ResistanceTimeSeries(ResistanceTimeSeriesType):
    """
    Time series of The measurement of the degree to which a substance opposes the
    passage of an electric current.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class RotaryVelocityTimeSeries(RotaryVelocityTimeSeriesType):
    """
    Time series of The measurement of the rotational speed of a rotary axis.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class SoundLevelTimeSeries(SoundLevelTimeSeriesType):
    """
    Time series of The measurement of a sound level or sound pressure level
    relative to atmospheric pressure.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class SpindleSpeedTimeSeries(SpindleSpeedTimeSeriesType):
    """Time series of **DEPRECATED** in *Version 1.2*.

    Replaced by {{block(RotaryVelocity)}}. The rotational speed of the
    rotary axis.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class StrainTimeSeries(StrainTimeSeriesType):
    """
    Time series of The measurement of the amount of deformation per unit length of
    an object when a load is applied.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class TemperatureTimeSeries(TemperatureTimeSeriesType):
    """
    Time series of The measurement of temperature.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class TensionTimeSeries(TensionTimeSeriesType):
    """
    Time series of The measurement of a force that stretches or elongates an
    object.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class TiltTimeSeries(TiltTimeSeriesType):
    """
    Time series of The measurement of angular displacement.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class ToolAssetIdDiscrete(ToolAssetIdDiscreteType):
    """
    Discrete of The identifier of an individual tool asset.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class ToolIdDiscrete(ToolIdDiscreteType):
    """Discrete of **DEPRECATED** in *Version 1.2.0*.

    See
    {{block(ToolAssetId)}}. The identifier of the tool currently in use for
    a given `Path`.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class ToolNumberDiscrete(ToolNumberDiscreteType):
    """
    Discrete of The identifier assigned by the {{block(Controller)}} component to a
    cutting tool when in use by a piece of equipment.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class TorqueTimeSeries(TorqueTimeSeriesType):
    """
    Time series of The measurement of the turning force exerted on an object or by
    an object.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class VelocityTimeSeries(VelocityTimeSeriesType):
    """
    Time series of The measurement of the rate of change of position of a
    {{block(Component)}}.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class ViscosityTimeSeries(ViscosityTimeSeriesType):
    """
    Time series of The measurement of a fluids resistance to flow.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class VoltAmpereReactiveTimeSeries(VoltAmpereReactiveTimeSeriesType):
    """
    Time series of The measurement of reactive power in an AC electrical circuit
    (commonly referred to as VAR).
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class VoltAmpereTimeSeries(VoltAmpereTimeSeriesType):
    """
    Time series of The measurement of the apparent power in an electrical circuit,
    equal to the product of root-mean-square (RMS) voltage and RMS current
    (commonly referred to as VA).
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class VoltageActimeSeries(VoltageActimeSeriesType):
    """
    Time series of The measurement of the electrical potential between two points
    in an electrical circuit in which the current periodically reverses direction.
    """

    class Meta:
        name = "VoltageACTimeSeries"
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class VoltageDctimeSeries(VoltageDctimeSeriesType):
    """
    Time series of The measurement of the electrical potential between two points
    in an electrical circuit in which the current is unidirectional.
    """

    class Meta:
        name = "VoltageDCTimeSeries"
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class VoltageTimeSeries(VoltageTimeSeriesType):
    """Time series of **DEPRECATED** in *Version 1.6*.

    Replaced by {{block(VoltageAC)}} and {{block(VoltageDC)}}. The
    measurement of electrical potential between two points.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class VolumeFluidTimeSeries(VolumeFluidTimeSeriesType):
    """
    Time series of The fluid volume of an object or container.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class VolumeSpatialTimeSeries(VolumeSpatialTimeSeriesType):
    """
    Time series of The geometric volume of an object or container.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class WattageTimeSeries(WattageTimeSeriesType):
    """
    Time series of The measurement of power flowing through or dissipated by an
    electrical circuit or piece of equipment.
    """

    class Meta:
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class XdimensionTimeSeries(XdimensionTimeSeriesType):
    """
    Time series of Measured dimension of an entity relative to the X direction of
    the referenced coordinate system.
    """

    class Meta:
        name = "XDimensionTimeSeries"
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class YdimensionTimeSeries(YdimensionTimeSeriesType):
    """
    Time series of Measured dimension of an entity relative to the Y direction of
    the referenced coordinate system.
    """

    class Meta:
        name = "YDimensionTimeSeries"
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class ZdimensionTimeSeries(ZdimensionTimeSeriesType):
    """
    Time series of Measured dimension of an entity relative to the Z direction of
    the referenced coordinate system.
    """

    class Meta:
        name = "ZDimensionTimeSeries"
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"


@dataclass
class EventsType:
    """{{block(Events)}} {{termplural(organize)}} the {{block(Event)}} elements.

    See {{sect(Event)}} for details on the {{block(Event)}} model.
    """

    tool_offset_table: List[ToolOffsetTable] = field(
        default_factory=list,
        metadata={
            "name": "ToolOffsetTable",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    work_offset_table: List[WorkOffsetTable] = field(
        default_factory=list,
        metadata={
            "name": "WorkOffsetTable",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    variable_data_set: List[VariableDataSet] = field(
        default_factory=list,
        metadata={
            "name": "VariableDataSet",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    connection_status: List[ConnectionStatus] = field(
        default_factory=list,
        metadata={
            "name": "ConnectionStatus",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    part_status: List[PartStatus] = field(
        default_factory=list,
        metadata={
            "name": "PartStatus",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    wait_state: List[WaitState] = field(
        default_factory=list,
        metadata={
            "name": "WaitState",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    spindle_interlock: List[SpindleInterlock] = field(
        default_factory=list,
        metadata={
            "name": "SpindleInterlock",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    rotary_mode: List[RotaryMode] = field(
        default_factory=list,
        metadata={
            "name": "RotaryMode",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    program_edit: List[ProgramEdit] = field(
        default_factory=list,
        metadata={
            "name": "ProgramEdit",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    power_state: List[PowerState] = field(
        default_factory=list,
        metadata={
            "name": "PowerState",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    path_mode: List[PathMode] = field(
        default_factory=list,
        metadata={
            "name": "PathMode",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    part_detect: List[PartDetect] = field(
        default_factory=list,
        metadata={
            "name": "PartDetect",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    interface_state: List[InterfaceState] = field(
        default_factory=list,
        metadata={
            "name": "InterfaceState",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    functional_mode: List[FunctionalMode] = field(
        default_factory=list,
        metadata={
            "name": "FunctionalMode",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    execution: List[Execution] = field(
        default_factory=list,
        metadata={
            "name": "Execution",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    equipment_mode: List[EquipmentMode] = field(
        default_factory=list,
        metadata={
            "name": "EquipmentMode",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    end_of_bar: List[EndOfBar] = field(
        default_factory=list,
        metadata={
            "name": "EndOfBar",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    emergency_stop: List[EmergencyStop] = field(
        default_factory=list,
        metadata={
            "name": "EmergencyStop",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    door_state: List[DoorState] = field(
        default_factory=list,
        metadata={
            "name": "DoorState",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    controller_mode_override: List[ControllerModeOverride] = field(
        default_factory=list,
        metadata={
            "name": "ControllerModeOverride",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    controller_mode: List[ControllerMode] = field(
        default_factory=list,
        metadata={
            "name": "ControllerMode",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    chuck_state: List[ChuckState] = field(
        default_factory=list,
        metadata={
            "name": "ChuckState",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    chuck_interlock: List[ChuckInterlock] = field(
        default_factory=list,
        metadata={
            "name": "ChuckInterlock",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    axis_state: List[AxisState] = field(
        default_factory=list,
        metadata={
            "name": "AxisState",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    axis_interlock: List[AxisInterlock] = field(
        default_factory=list,
        metadata={
            "name": "AxisInterlock",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    axis_coupling: List[AxisCoupling] = field(
        default_factory=list,
        metadata={
            "name": "AxisCoupling",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    availability: List[Availability] = field(
        default_factory=list,
        metadata={
            "name": "Availability",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    actuator_state: List[ActuatorState] = field(
        default_factory=list,
        metadata={
            "name": "ActuatorState",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    work_offset: List[WorkOffset] = field(
        default_factory=list,
        metadata={
            "name": "WorkOffset",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    tool_offset: List[ToolOffset] = field(
        default_factory=list,
        metadata={
            "name": "ToolOffset",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    rotary_velocity_override: List[RotaryVelocityOverride] = field(
        default_factory=list,
        metadata={
            "name": "RotaryVelocityOverride",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    path_feedrate_override: List[PathFeedrateOverride] = field(
        default_factory=list,
        metadata={
            "name": "PathFeedrateOverride",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    part_count_discrete: List[PartCountDiscrete] = field(
        default_factory=list,
        metadata={
            "name": "PartCountDiscrete",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    part_count: List[PartCount] = field(
        default_factory=list,
        metadata={
            "name": "PartCount",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    hardness: List[Hardness] = field(
        default_factory=list,
        metadata={
            "name": "Hardness",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    axis_feedrate_override: List[AxisFeedrateOverride] = field(
        default_factory=list,
        metadata={
            "name": "AxisFeedrateOverride",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    float_event: List[FloatEvent] = field(
        default_factory=list,
        metadata={
            "name": "FloatEvent",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    program_nest_level: List[ProgramNestLevel] = field(
        default_factory=list,
        metadata={
            "name": "ProgramNestLevel",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    material_layer: List[MaterialLayer] = field(
        default_factory=list,
        metadata={
            "name": "MaterialLayer",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    line_number: List[LineNumber] = field(
        default_factory=list,
        metadata={
            "name": "LineNumber",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    block_count: List[BlockCount] = field(
        default_factory=list,
        metadata={
            "name": "BlockCount",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    integer_event: List[IntegerEvent] = field(
        default_factory=list,
        metadata={
            "name": "IntegerEvent",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    coupled_axes: List[CoupledAxes] = field(
        default_factory=list,
        metadata={
            "name": "CoupledAxes",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    active_axes: List[ActiveAxes] = field(
        default_factory=list,
        metadata={
            "name": "ActiveAxes",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    string_list_event: List[StringListEvent] = field(
        default_factory=list,
        metadata={
            "name": "StringListEvent",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    alarm: List[Alarm] = field(
        default_factory=list,
        metadata={
            "name": "Alarm",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    part_unique_id: List[PartUniqueId] = field(
        default_factory=list,
        metadata={
            "name": "PartUniqueId",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    part_group_id: List[PartGroupId] = field(
        default_factory=list,
        metadata={
            "name": "PartGroupId",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    process_occurrence_id: List[ProcessOccurrenceId] = field(
        default_factory=list,
        metadata={
            "name": "ProcessOccurrenceId",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    mtconnect_version: List[MtconnectVersion] = field(
        default_factory=list,
        metadata={
            "name": "MTConnectVersion",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    device_added: List[DeviceAdded] = field(
        default_factory=list,
        metadata={
            "name": "DeviceAdded",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    control_limit: List[ControlLimit] = field(
        default_factory=list,
        metadata={
            "name": "ControlLimit",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    sensor_attachment: List[SensorAttachment] = field(
        default_factory=list,
        metadata={
            "name": "SensorAttachment",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    adapter_software_version: List[AdapterSoftwareVersion] = field(
        default_factory=list,
        metadata={
            "name": "AdapterSoftwareVersion",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    specification_limit: List[SpecificationLimit] = field(
        default_factory=list,
        metadata={
            "name": "SpecificationLimit",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    device_changed: List[DeviceChanged] = field(
        default_factory=list,
        metadata={
            "name": "DeviceChanged",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    device_removed: List[DeviceRemoved] = field(
        default_factory=list,
        metadata={
            "name": "DeviceRemoved",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    adapter_uri: List[AdapterUri] = field(
        default_factory=list,
        metadata={
            "name": "AdapterURI",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    part_kind_id: List[PartKindId] = field(
        default_factory=list,
        metadata={
            "name": "PartKindId",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    process_aggregate_id: List[ProcessAggregateId] = field(
        default_factory=list,
        metadata={
            "name": "ProcessAggregateId",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    alarm_limit: List[AlarmLimit] = field(
        default_factory=list,
        metadata={
            "name": "AlarmLimit",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    process_kind_id: List[ProcessKindId] = field(
        default_factory=list,
        metadata={
            "name": "ProcessKindId",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    translation: List[Translation] = field(
        default_factory=list,
        metadata={
            "name": "Translation",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    rotation: List[Rotation] = field(
        default_factory=list,
        metadata={
            "name": "Rotation",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    network: List[Network] = field(
        default_factory=list,
        metadata={
            "name": "Network",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    hardware: List[Hardware] = field(
        default_factory=list,
        metadata={
            "name": "Hardware",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    library: List[Library] = field(
        default_factory=list,
        metadata={
            "name": "Library",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    application: List[Application] = field(
        default_factory=list,
        metadata={
            "name": "Application",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    firmware: List[Firmware] = field(
        default_factory=list,
        metadata={
            "name": "Firmware",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    operating_system: List[OperatingSystem] = field(
        default_factory=list,
        metadata={
            "name": "OperatingSystem",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    workholding_id: List[WorkholdingId] = field(
        default_factory=list,
        metadata={
            "name": "WorkholdingId",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    wire: List[Wire] = field(
        default_factory=list,
        metadata={
            "name": "Wire",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    variable: List[Variable] = field(
        default_factory=list,
        metadata={
            "name": "Variable",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    user: List[User] = field(
        default_factory=list,
        metadata={
            "name": "User",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    tool_number_discrete: List[ToolNumberDiscrete] = field(
        default_factory=list,
        metadata={
            "name": "ToolNumberDiscrete",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    tool_number: List[ToolNumber] = field(
        default_factory=list,
        metadata={
            "name": "ToolNumber",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    tool_id_discrete: List[ToolIdDiscrete] = field(
        default_factory=list,
        metadata={
            "name": "ToolIdDiscrete",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    tool_id: List[ToolId] = field(
        default_factory=list,
        metadata={
            "name": "ToolId",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    tool_group: List[ToolGroup] = field(
        default_factory=list,
        metadata={
            "name": "ToolGroup",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    tool_asset_id_discrete: List[ToolAssetIdDiscrete] = field(
        default_factory=list,
        metadata={
            "name": "ToolAssetIdDiscrete",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    tool_asset_id: List[ToolAssetId] = field(
        default_factory=list,
        metadata={
            "name": "ToolAssetId",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    serial_number: List[SerialNumber] = field(
        default_factory=list,
        metadata={
            "name": "SerialNumber",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    program_location: List[ProgramLocation] = field(
        default_factory=list,
        metadata={
            "name": "ProgramLocation",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    program_header: List[ProgramHeader] = field(
        default_factory=list,
        metadata={
            "name": "ProgramHeader",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    program_edit_name: List[ProgramEditName] = field(
        default_factory=list,
        metadata={
            "name": "ProgramEditName",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    program_comment: List[ProgramComment] = field(
        default_factory=list,
        metadata={
            "name": "ProgramComment",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    program: List[Program] = field(
        default_factory=list,
        metadata={
            "name": "Program",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    process_time: List[ProcessTime] = field(
        default_factory=list,
        metadata={
            "name": "ProcessTime",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    power_status: List[PowerStatus] = field(
        default_factory=list,
        metadata={
            "name": "PowerStatus",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    part_number: List[PartNumber] = field(
        default_factory=list,
        metadata={
            "name": "PartNumber",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    part_id: List[PartId] = field(
        default_factory=list,
        metadata={
            "name": "PartId",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    part_change: List[PartChange] = field(
        default_factory=list,
        metadata={
            "name": "PartChange",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    pallet_id_discrete: List[PalletIdDiscrete] = field(
        default_factory=list,
        metadata={
            "name": "PalletIdDiscrete",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    pallet_id: List[PalletId] = field(
        default_factory=list,
        metadata={
            "name": "PalletId",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    operator_id: List[OperatorId] = field(
        default_factory=list,
        metadata={
            "name": "OperatorId",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    open_door: List[OpenDoor] = field(
        default_factory=list,
        metadata={
            "name": "OpenDoor",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    open_chuck: List[OpenChuck] = field(
        default_factory=list,
        metadata={
            "name": "OpenChuck",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    message_discrete: List[MessageDiscrete] = field(
        default_factory=list,
        metadata={
            "name": "MessageDiscrete",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    message: List[Message] = field(
        default_factory=list,
        metadata={
            "name": "Message",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    material_unload: List[MaterialUnload] = field(
        default_factory=list,
        metadata={
            "name": "MaterialUnload",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    material_retract: List[MaterialRetract] = field(
        default_factory=list,
        metadata={
            "name": "MaterialRetract",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    material_load: List[MaterialLoad] = field(
        default_factory=list,
        metadata={
            "name": "MaterialLoad",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    material_feed: List[MaterialFeed] = field(
        default_factory=list,
        metadata={
            "name": "MaterialFeed",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    material_change: List[MaterialChange] = field(
        default_factory=list,
        metadata={
            "name": "MaterialChange",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    material: List[Material] = field(
        default_factory=list,
        metadata={
            "name": "Material",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    line_label: List[LineLabel] = field(
        default_factory=list,
        metadata={
            "name": "LineLabel",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    line: List[Line] = field(
        default_factory=list,
        metadata={
            "name": "Line",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    direction: List[Direction] = field(
        default_factory=list,
        metadata={
            "name": "Direction",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    device_uuid: List[DeviceUuid] = field(
        default_factory=list,
        metadata={
            "name": "DeviceUuid",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    date_code: List[DateCode] = field(
        default_factory=list,
        metadata={
            "name": "DateCode",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    composition_state: List[CompositionState] = field(
        default_factory=list,
        metadata={
            "name": "CompositionState",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    code: List[Code] = field(
        default_factory=list,
        metadata={
            "name": "Code",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    close_door: List[CloseDoor] = field(
        default_factory=list,
        metadata={
            "name": "CloseDoor",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    close_chuck: List[CloseChuck] = field(
        default_factory=list,
        metadata={
            "name": "CloseChuck",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    block_discrete: List[BlockDiscrete] = field(
        default_factory=list,
        metadata={
            "name": "BlockDiscrete",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    block: List[Block] = field(
        default_factory=list,
        metadata={
            "name": "Block",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    asset_removed: List[AssetRemoved] = field(
        default_factory=list,
        metadata={
            "name": "AssetRemoved",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    asset_changed: List[AssetChanged] = field(
        default_factory=list,
        metadata={
            "name": "AssetChanged",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    program_location_type: List[ProgramLocationType] = field(
        default_factory=list,
        metadata={
            "name": "ProgramLocationType",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    string_event: List[StringEvent] = field(
        default_factory=list,
        metadata={
            "name": "StringEvent",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )


@dataclass
class SamplesType:
    """{{block(Samples)}} {{termplural(organize)}} the {{block(Sample)}} elements.

    See {{sect(Sample)}} for details on the {{block(Sample)}} model.
    """

    pressure_absolute_time_series: List[PressureAbsoluteTimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "PressureAbsoluteTimeSeries",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    observation_update_rate_time_series: List[
        ObservationUpdateRateTimeSeries
    ] = field(
        default_factory=list,
        metadata={
            "name": "ObservationUpdateRateTimeSeries",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    angular_deceleration_time_series: List[AngularDecelerationTimeSeries] = (
        field(
            default_factory=list,
            metadata={
                "name": "AngularDecelerationTimeSeries",
                "type": "Element",
                "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
            },
        )
    )
    asset_update_rate_time_series: List[AssetUpdateRateTimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "AssetUpdateRateTimeSeries",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    deceleration_time_series: List[DecelerationTimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "DecelerationTimeSeries",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    pressurization_rate_time_series: List[PressurizationRateTimeSeries] = (
        field(
            default_factory=list,
            metadata={
                "name": "PressurizationRateTimeSeries",
                "type": "Element",
                "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
            },
        )
    )
    humidity_specific_time_series: List[HumiditySpecificTimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "HumiditySpecificTimeSeries",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    humidity_absolute_time_series: List[HumidityAbsoluteTimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "HumidityAbsoluteTimeSeries",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    humidity_relative_time_series: List[HumidityRelativeTimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "HumidityRelativeTimeSeries",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    diameter_time_series: List[DiameterTimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "DiameterTimeSeries",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    zdimension_time_series: List[ZdimensionTimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "ZDimensionTimeSeries",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    ydimension_time_series: List[YdimensionTimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "YDimensionTimeSeries",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    xdimension_time_series: List[XdimensionTimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "XDimensionTimeSeries",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    voltage_dctime_series: List[VoltageDctimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "VoltageDCTimeSeries",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    voltage_actime_series: List[VoltageActimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "VoltageACTimeSeries",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    amperage_actime_series: List[AmperageActimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "AmperageACTimeSeries",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    amperage_dctime_series: List[AmperageDctimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "AmperageDCTimeSeries",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    wattage_time_series: List[WattageTimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "WattageTimeSeries",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    volume_spatial_time_series: List[VolumeSpatialTimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "VolumeSpatialTimeSeries",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    volume_fluid_time_series: List[VolumeFluidTimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "VolumeFluidTimeSeries",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    volt_ampere_reactive_time_series: List[VoltAmpereReactiveTimeSeries] = (
        field(
            default_factory=list,
            metadata={
                "name": "VoltAmpereReactiveTimeSeries",
                "type": "Element",
                "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
            },
        )
    )
    volt_ampere_time_series: List[VoltAmpereTimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "VoltAmpereTimeSeries",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    voltage_time_series: List[VoltageTimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "VoltageTimeSeries",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    viscosity_time_series: List[ViscosityTimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "ViscosityTimeSeries",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    velocity_time_series: List[VelocityTimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "VelocityTimeSeries",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    torque_time_series: List[TorqueTimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "TorqueTimeSeries",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    tilt_time_series: List[TiltTimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "TiltTimeSeries",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    tension_time_series: List[TensionTimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "TensionTimeSeries",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    temperature_time_series: List[TemperatureTimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "TemperatureTimeSeries",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    strain_time_series: List[StrainTimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "StrainTimeSeries",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    spindle_speed_time_series: List[SpindleSpeedTimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "SpindleSpeedTimeSeries",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    sound_level_time_series: List[SoundLevelTimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "SoundLevelTimeSeries",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    rotary_velocity_time_series: List[RotaryVelocityTimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "RotaryVelocityTimeSeries",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    resistance_time_series: List[ResistanceTimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "ResistanceTimeSeries",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    process_timer_time_series: List[ProcessTimerTimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "ProcessTimerTimeSeries",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    pressure_time_series: List[PressureTimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "PressureTimeSeries",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    power_factor_time_series: List[PowerFactorTimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "PowerFactorTimeSeries",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    position_time_series: List[PositionTimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "PositionTimeSeries",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    phtime_series: List[PhtimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "PHTimeSeries",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    path_feedrate_per_revolution_time_series: List[
        PathFeedratePerRevolutionTimeSeries
    ] = field(
        default_factory=list,
        metadata={
            "name": "PathFeedratePerRevolutionTimeSeries",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    path_feedrate_time_series: List[PathFeedrateTimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "PathFeedrateTimeSeries",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    mass_time_series: List[MassTimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "MassTimeSeries",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    load_time_series: List[LoadTimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "LoadTimeSeries",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    linear_force_time_series: List[LinearForceTimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "LinearForceTimeSeries",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    level_time_series: List[LevelTimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "LevelTimeSeries",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    length_time_series: List[LengthTimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "LengthTimeSeries",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    global_position_time_series: List[GlobalPositionTimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "GlobalPositionTimeSeries",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    frequency_time_series: List[FrequencyTimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "FrequencyTimeSeries",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    flow_time_series: List[FlowTimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "FlowTimeSeries",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    fill_level_time_series: List[FillLevelTimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "FillLevelTimeSeries",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    equipment_timer_time_series: List[EquipmentTimerTimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "EquipmentTimerTimeSeries",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    electrical_energy_time_series: List[ElectricalEnergyTimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "ElectricalEnergyTimeSeries",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    displacement_time_series: List[DisplacementTimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "DisplacementTimeSeries",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    deposition_volume_time_series: List[DepositionVolumeTimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "DepositionVolumeTimeSeries",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    deposition_rate_volumetric_time_series: List[
        DepositionRateVolumetricTimeSeries
    ] = field(
        default_factory=list,
        metadata={
            "name": "DepositionRateVolumetricTimeSeries",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    deposition_mass_time_series: List[DepositionMassTimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "DepositionMassTimeSeries",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    deposition_density_time_series: List[DepositionDensityTimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "DepositionDensityTimeSeries",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    deposition_acceleration_volumetric_time_series: List[
        DepositionAccelerationVolumetricTimeSeries
    ] = field(
        default_factory=list,
        metadata={
            "name": "DepositionAccelerationVolumetricTimeSeries",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    density_time_series: List[DensityTimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "DensityTimeSeries",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    cutting_speed_time_series: List[CuttingSpeedTimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "CuttingSpeedTimeSeries",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    conductivity_time_series: List[ConductivityTimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "ConductivityTimeSeries",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    concentration_time_series: List[ConcentrationTimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "ConcentrationTimeSeries",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    clock_time_time_series: List[ClockTimeTimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "ClockTimeTimeSeries",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    capacity_spatial_time_series: List[CapacitySpatialTimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "CapacitySpatialTimeSeries",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    capacity_fluid_time_series: List[CapacityFluidTimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "CapacityFluidTimeSeries",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    axis_feedrate_time_series: List[AxisFeedrateTimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "AxisFeedrateTimeSeries",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    angular_velocity_time_series: List[AngularVelocityTimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "AngularVelocityTimeSeries",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    angular_acceleration_time_series: List[AngularAccelerationTimeSeries] = (
        field(
            default_factory=list,
            metadata={
                "name": "AngularAccelerationTimeSeries",
                "type": "Element",
                "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
            },
        )
    )
    angle_time_series: List[AngleTimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "AngleTimeSeries",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    amperage_time_series: List[AmperageTimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "AmperageTimeSeries",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    accumulated_time_time_series: List[AccumulatedTimeTimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "AccumulatedTimeTimeSeries",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    acceleration_time_series: List[AccelerationTimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "AccelerationTimeSeries",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    orientation: List[Orientation] = field(
        default_factory=list,
        metadata={
            "name": "Orientation",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    path_position: List[PathPosition] = field(
        default_factory=list,
        metadata={
            "name": "PathPosition",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    three_space_sample: List[ThreeSpaceSample] = field(
        default_factory=list,
        metadata={
            "name": "ThreeSpaceSample",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    pressure_absolute: List[PressureAbsolute] = field(
        default_factory=list,
        metadata={
            "name": "PressureAbsolute",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    observation_update_rate: List[ObservationUpdateRate] = field(
        default_factory=list,
        metadata={
            "name": "ObservationUpdateRate",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    angular_deceleration: List[AngularDeceleration] = field(
        default_factory=list,
        metadata={
            "name": "AngularDeceleration",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    asset_update_rate: List[AssetUpdateRate] = field(
        default_factory=list,
        metadata={
            "name": "AssetUpdateRate",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    deceleration: List[Deceleration] = field(
        default_factory=list,
        metadata={
            "name": "Deceleration",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    pressurization_rate: List[PressurizationRate] = field(
        default_factory=list,
        metadata={
            "name": "PressurizationRate",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    humidity_specific: List[HumiditySpecific] = field(
        default_factory=list,
        metadata={
            "name": "HumiditySpecific",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    humidity_absolute: List[HumidityAbsolute] = field(
        default_factory=list,
        metadata={
            "name": "HumidityAbsolute",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    humidity_relative: List[HumidityRelative] = field(
        default_factory=list,
        metadata={
            "name": "HumidityRelative",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    diameter: List[Diameter] = field(
        default_factory=list,
        metadata={
            "name": "Diameter",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    zdimension: List[Zdimension] = field(
        default_factory=list,
        metadata={
            "name": "ZDimension",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    ydimension: List[Ydimension] = field(
        default_factory=list,
        metadata={
            "name": "YDimension",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    xdimension: List[Xdimension] = field(
        default_factory=list,
        metadata={
            "name": "XDimension",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    voltage_dc: List[VoltageDc] = field(
        default_factory=list,
        metadata={
            "name": "VoltageDC",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    voltage_ac: List[VoltageAc] = field(
        default_factory=list,
        metadata={
            "name": "VoltageAC",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    amperage_ac: List[AmperageAc] = field(
        default_factory=list,
        metadata={
            "name": "AmperageAC",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    amperage_dc: List[AmperageDc] = field(
        default_factory=list,
        metadata={
            "name": "AmperageDC",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    wattage: List[Wattage] = field(
        default_factory=list,
        metadata={
            "name": "Wattage",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    volume_spatial: List[VolumeSpatial] = field(
        default_factory=list,
        metadata={
            "name": "VolumeSpatial",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    volume_fluid: List[VolumeFluid] = field(
        default_factory=list,
        metadata={
            "name": "VolumeFluid",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    volt_ampere_reactive: List[VoltAmpereReactive] = field(
        default_factory=list,
        metadata={
            "name": "VoltAmpereReactive",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    volt_ampere: List[VoltAmpere] = field(
        default_factory=list,
        metadata={
            "name": "VoltAmpere",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    voltage: List[Voltage] = field(
        default_factory=list,
        metadata={
            "name": "Voltage",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    viscosity: List[Viscosity] = field(
        default_factory=list,
        metadata={
            "name": "Viscosity",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    velocity: List[Velocity] = field(
        default_factory=list,
        metadata={
            "name": "Velocity",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    torque: List[Torque] = field(
        default_factory=list,
        metadata={
            "name": "Torque",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    tilt: List[Tilt] = field(
        default_factory=list,
        metadata={
            "name": "Tilt",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    tension: List[Tension] = field(
        default_factory=list,
        metadata={
            "name": "Tension",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    temperature: List[Temperature] = field(
        default_factory=list,
        metadata={
            "name": "Temperature",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    strain: List[Strain] = field(
        default_factory=list,
        metadata={
            "name": "Strain",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    spindle_speed: List[SpindleSpeed] = field(
        default_factory=list,
        metadata={
            "name": "SpindleSpeed",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    sound_level: List[SoundLevel] = field(
        default_factory=list,
        metadata={
            "name": "SoundLevel",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    rotary_velocity: List[RotaryVelocity] = field(
        default_factory=list,
        metadata={
            "name": "RotaryVelocity",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    resistance: List[Resistance] = field(
        default_factory=list,
        metadata={
            "name": "Resistance",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    process_timer: List[ProcessTimer] = field(
        default_factory=list,
        metadata={
            "name": "ProcessTimer",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    pressure: List[Pressure] = field(
        default_factory=list,
        metadata={
            "name": "Pressure",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    power_factor: List[PowerFactor] = field(
        default_factory=list,
        metadata={
            "name": "PowerFactor",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    position: List[Position] = field(
        default_factory=list,
        metadata={
            "name": "Position",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    ph: List[Ph] = field(
        default_factory=list,
        metadata={
            "name": "PH",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    path_feedrate_per_revolution: List[PathFeedratePerRevolution] = field(
        default_factory=list,
        metadata={
            "name": "PathFeedratePerRevolution",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    path_feedrate: List[PathFeedrate] = field(
        default_factory=list,
        metadata={
            "name": "PathFeedrate",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    mass: List[Mass] = field(
        default_factory=list,
        metadata={
            "name": "Mass",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    load: List[Load] = field(
        default_factory=list,
        metadata={
            "name": "Load",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    linear_force: List[LinearForce] = field(
        default_factory=list,
        metadata={
            "name": "LinearForce",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    level: List[Level] = field(
        default_factory=list,
        metadata={
            "name": "Level",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    length: List[Length] = field(
        default_factory=list,
        metadata={
            "name": "Length",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    global_position: List[GlobalPosition] = field(
        default_factory=list,
        metadata={
            "name": "GlobalPosition",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    frequency: List[Frequency] = field(
        default_factory=list,
        metadata={
            "name": "Frequency",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    flow: List[Flow] = field(
        default_factory=list,
        metadata={
            "name": "Flow",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    fill_level: List[FillLevel] = field(
        default_factory=list,
        metadata={
            "name": "FillLevel",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    equipment_timer: List[EquipmentTimer] = field(
        default_factory=list,
        metadata={
            "name": "EquipmentTimer",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    electrical_energy: List[ElectricalEnergy] = field(
        default_factory=list,
        metadata={
            "name": "ElectricalEnergy",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    displacement: List[Displacement] = field(
        default_factory=list,
        metadata={
            "name": "Displacement",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    deposition_volume: List[DepositionVolume] = field(
        default_factory=list,
        metadata={
            "name": "DepositionVolume",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    deposition_rate_volumetric: List[DepositionRateVolumetric] = field(
        default_factory=list,
        metadata={
            "name": "DepositionRateVolumetric",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    deposition_mass: List[DepositionMass] = field(
        default_factory=list,
        metadata={
            "name": "DepositionMass",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    deposition_density: List[DepositionDensity] = field(
        default_factory=list,
        metadata={
            "name": "DepositionDensity",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    deposition_acceleration_volumetric: List[
        DepositionAccelerationVolumetric
    ] = field(
        default_factory=list,
        metadata={
            "name": "DepositionAccelerationVolumetric",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    density: List[Density] = field(
        default_factory=list,
        metadata={
            "name": "Density",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    cutting_speed: List[CuttingSpeed] = field(
        default_factory=list,
        metadata={
            "name": "CuttingSpeed",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    conductivity: List[Conductivity] = field(
        default_factory=list,
        metadata={
            "name": "Conductivity",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    concentration: List[Concentration] = field(
        default_factory=list,
        metadata={
            "name": "Concentration",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    clock_time: List[ClockTime] = field(
        default_factory=list,
        metadata={
            "name": "ClockTime",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    capacity_spatial: List[CapacitySpatial] = field(
        default_factory=list,
        metadata={
            "name": "CapacitySpatial",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    capacity_fluid: List[CapacityFluid] = field(
        default_factory=list,
        metadata={
            "name": "CapacityFluid",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    axis_feedrate: List[AxisFeedrate] = field(
        default_factory=list,
        metadata={
            "name": "AxisFeedrate",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    angular_velocity: List[AngularVelocity] = field(
        default_factory=list,
        metadata={
            "name": "AngularVelocity",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    angular_acceleration: List[AngularAcceleration] = field(
        default_factory=list,
        metadata={
            "name": "AngularAcceleration",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    angle: List[Angle] = field(
        default_factory=list,
        metadata={
            "name": "Angle",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    amperage: List[Amperage] = field(
        default_factory=list,
        metadata={
            "name": "Amperage",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    accumulated_time: List[AccumulatedTime] = field(
        default_factory=list,
        metadata={
            "name": "AccumulatedTime",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    acceleration: List[Acceleration] = field(
        default_factory=list,
        metadata={
            "name": "Acceleration",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    common_sample: List[CommonSample] = field(
        default_factory=list,
        metadata={
            "name": "CommonSample",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )


@dataclass
class ComponentStreamType:
    """
    See the following {{sect(ComponentStream)}} for details.

    :ivar samples: {{block(Samples)}} {{termplural(organize)}} the
        {{block(Sample)}} elements. See {{sect(Sample)}} for details on
        the {{block(Sample)}} model.
    :ivar events: {{block(Events)}} {{termplural(organize)}} the
        {{block(Event)}} elements. See {{sect(Event)}} for details on
        the {{block(Event)}} model.
    :ivar condition: An indicator of the ability of a piece of equipment
        or {{term(Component)}} to function to specification.
    :ivar component_id: The id of the component (maps to the id from
        probe)
    :ivar name: The component name
    :ivar native_name: The device manufacturer component name
    :ivar component: A {{term(Structural Element)}} that represents a
        physical or logical part or subpart of a piece of equipment.
    :ivar uuid: The unque identifier for this component
    """

    samples: Optional[SamplesType] = field(
        default=None,
        metadata={
            "name": "Samples",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    events: Optional[EventsType] = field(
        default=None,
        metadata={
            "name": "Events",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    condition: Optional[ConditionListType] = field(
        default=None,
        metadata={
            "name": "Condition",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    component_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "componentId",
            "type": "Attribute",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    native_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "nativeName",
            "type": "Attribute",
        },
    )
    component: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class DeviceStreamType:
    """{{block(DeviceStream)}} {{termplural(organize)}} data reported from a single
    piece of equipment.

    A {{block(DeviceStream)}} element **MUST** be provided for each
    piece of equipment reporting data in an {{block(MTConnectStreams)}}
    {{term(Response Document)}}.

    :ivar component_stream: See the following {{sect(ComponentStream)}}
        for details.
    :ivar name: The component name
    :ivar uuid: The unque identifier for this device
    """

    component_stream: List[ComponentStreamType] = field(
        default_factory=list,
        metadata={
            "name": "ComponentStream",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class StreamsType:
    """
    Structural Elements for MTConnectStreams.

    :ivar device_stream: {{block(DeviceStream)}}
        {{termplural(organize)}} data reported from a single piece of
        equipment. A {{block(DeviceStream)}} element **MUST** be
        provided for each piece of equipment reporting data in an
        {{block(MTConnectStreams)}} {{term(Response Document)}}.
    """

    device_stream: List[DeviceStreamType] = field(
        default_factory=list,
        metadata={
            "name": "DeviceStream",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
        },
    )


@dataclass
class MtconnectStreamsType:
    """
    The root node for MTConnect.

    :ivar header: Supplemental data usually placed at the beginning of a
        {{term(Document)}}.
    :ivar streams: Structural Elements for MTConnectStreams
    """

    class Meta:
        name = "MTConnectStreamsType"

    header: Optional[HeaderType] = field(
        default=None,
        metadata={
            "name": "Header",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
            "required": True,
        },
    )
    streams: Optional[StreamsType] = field(
        default=None,
        metadata={
            "name": "Streams",
            "type": "Element",
            "namespace": "urn:mtconnect.org:MTConnectStreams:1.7",
            "required": True,
        },
    )


@dataclass
class MtconnectStreams(MtconnectStreamsType):
    """
    The root node for MTConnect.
    """

    class Meta:
        name = "MTConnectStreams"
        namespace = "urn:mtconnect.org:MTConnectStreams:1.7"
