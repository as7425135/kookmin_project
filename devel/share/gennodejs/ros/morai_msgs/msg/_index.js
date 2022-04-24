
"use strict";

let EgoVehicleStatus = require('./EgoVehicleStatus.js');
let MoraiTLIndex = require('./MoraiTLIndex.js');
let WaitForTickResponse = require('./WaitForTickResponse.js');
let WaitForTick = require('./WaitForTick.js');
let IntersectionControl = require('./IntersectionControl.js');
let ERP42Info = require('./ERP42Info.js');
let SyncModeCmd = require('./SyncModeCmd.js');
let SyncModeCmdResponse = require('./SyncModeCmdResponse.js');
let MoraiSimProcStatus = require('./MoraiSimProcStatus.js');
let SensorPosControl = require('./SensorPosControl.js');
let MultiEgoSetting = require('./MultiEgoSetting.js');
let IntscnTL = require('./IntscnTL.js');
let GetTrafficLightStatus = require('./GetTrafficLightStatus.js');
let SyncModeSetGear = require('./SyncModeSetGear.js');
let GPSMessage = require('./GPSMessage.js');
let PRCtrlCmd = require('./PRCtrlCmd.js');
let SyncModeCtrlCmd = require('./SyncModeCtrlCmd.js');
let SaveSensorData = require('./SaveSensorData.js');
let MoraiTLInfo = require('./MoraiTLInfo.js');
let Lamps = require('./Lamps.js');
let GhostMessage = require('./GhostMessage.js');
let PRStatus = require('./PRStatus.js');
let VehicleSpecIndex = require('./VehicleSpecIndex.js');
let ScenarioLoad = require('./ScenarioLoad.js');
let PREvent = require('./PREvent.js');
let ReplayInfo = require('./ReplayInfo.js');
let MoraiSrvResponse = require('./MoraiSrvResponse.js');
let ObjectStatusList = require('./ObjectStatusList.js');
let VehicleSpec = require('./VehicleSpec.js');
let RadarTrack = require('./RadarTrack.js');
let VehicleCollision = require('./VehicleCollision.js');
let SyncModeAddObj = require('./SyncModeAddObj.js');
let RadarTracks = require('./RadarTracks.js');
let SyncModeRemoveObj = require('./SyncModeRemoveObj.js');
let CtrlCmd = require('./CtrlCmd.js');
let MapSpecIndex = require('./MapSpecIndex.js');
let IntersectionStatus = require('./IntersectionStatus.js');
let NpcGhostInfo = require('./NpcGhostInfo.js');
let MapSpec = require('./MapSpec.js');
let ObjectStatus = require('./ObjectStatus.js');
let MoraiSimProcHandle = require('./MoraiSimProcHandle.js');
let CollisionData = require('./CollisionData.js');
let SyncModeResultResponse = require('./SyncModeResultResponse.js');
let TrafficLight = require('./TrafficLight.js');
let SetTrafficLight = require('./SetTrafficLight.js');
let VehicleCollisionData = require('./VehicleCollisionData.js');
let NpcGhostCmd = require('./NpcGhostCmd.js');
let SyncModeInfo = require('./SyncModeInfo.js');
let EventInfo = require('./EventInfo.js');
let SyncModeScenarioLoad = require('./SyncModeScenarioLoad.js');

module.exports = {
  EgoVehicleStatus: EgoVehicleStatus,
  MoraiTLIndex: MoraiTLIndex,
  WaitForTickResponse: WaitForTickResponse,
  WaitForTick: WaitForTick,
  IntersectionControl: IntersectionControl,
  ERP42Info: ERP42Info,
  SyncModeCmd: SyncModeCmd,
  SyncModeCmdResponse: SyncModeCmdResponse,
  MoraiSimProcStatus: MoraiSimProcStatus,
  SensorPosControl: SensorPosControl,
  MultiEgoSetting: MultiEgoSetting,
  IntscnTL: IntscnTL,
  GetTrafficLightStatus: GetTrafficLightStatus,
  SyncModeSetGear: SyncModeSetGear,
  GPSMessage: GPSMessage,
  PRCtrlCmd: PRCtrlCmd,
  SyncModeCtrlCmd: SyncModeCtrlCmd,
  SaveSensorData: SaveSensorData,
  MoraiTLInfo: MoraiTLInfo,
  Lamps: Lamps,
  GhostMessage: GhostMessage,
  PRStatus: PRStatus,
  VehicleSpecIndex: VehicleSpecIndex,
  ScenarioLoad: ScenarioLoad,
  PREvent: PREvent,
  ReplayInfo: ReplayInfo,
  MoraiSrvResponse: MoraiSrvResponse,
  ObjectStatusList: ObjectStatusList,
  VehicleSpec: VehicleSpec,
  RadarTrack: RadarTrack,
  VehicleCollision: VehicleCollision,
  SyncModeAddObj: SyncModeAddObj,
  RadarTracks: RadarTracks,
  SyncModeRemoveObj: SyncModeRemoveObj,
  CtrlCmd: CtrlCmd,
  MapSpecIndex: MapSpecIndex,
  IntersectionStatus: IntersectionStatus,
  NpcGhostInfo: NpcGhostInfo,
  MapSpec: MapSpec,
  ObjectStatus: ObjectStatus,
  MoraiSimProcHandle: MoraiSimProcHandle,
  CollisionData: CollisionData,
  SyncModeResultResponse: SyncModeResultResponse,
  TrafficLight: TrafficLight,
  SetTrafficLight: SetTrafficLight,
  VehicleCollisionData: VehicleCollisionData,
  NpcGhostCmd: NpcGhostCmd,
  SyncModeInfo: SyncModeInfo,
  EventInfo: EventInfo,
  SyncModeScenarioLoad: SyncModeScenarioLoad,
};
