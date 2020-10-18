
/**
 * Returns an indicator behavior instance that corresponds to the given ID.
 * IDs are defined by the enumeration above.
 */
function createIndicatorBehavior(id) {
    switch (id) {
        case INDICATOR_ALARMS:
            return new AlarmsIndicatorBehavior();
        case INDICATOR_APPOINTMENTS:
            return new AppointmentIndicatorBehavior();
        case INDICATOR_BATTERY:
            return new BatteryIndicatorBehavior();
        case INDICATOR_BLUETOOTH:
            return new BluetoothIndicatorBehavior();
        case INDICATOR_DND:
            return new DoNotDisturbIndicatorBehavior();
        case INDICATOR_HEART_RATE:
            return new HeartRateIndicatorBehavior();
        case INDICATOR_NOTIFICATIONS:
            return new NotificationsIndicatorBehavior();
        default:
            return null;
    }
}

/**
 * Returns a meter behavior instance that corresponds to the given ID.
 * IDs are defined by the enumeration above.
 */
function createMeterBehavior(id) {
    switch (id) {
        case METER_ACTIVE_MINUTES:
            return new ActiveMinutesMeterBehavior();
        case METER_BATTERY:
            return new BatteryMeterBehavior();
        case METER_MOVE_BAR:
            return new MoveBarMeterBehavior();
        case METER_FLOORS_CLIMBED:
            return new FloorsClimbedMeterBehavior();
        case METER_STEPS:
            return new StepsMeterBehavior();
        default:
            return null;
    }
}
