from pyais import decode

# 原始AIS数据（包含时间戳）
ais_data_with_timestamp = "2018-04-20 08:00:00.082: !AIVDO,1,1,,,16:kpR00298lKHdDlgjv2;>40000,0*79"
# 分离时间戳和AIS消息
timestamp, ais_data = ais_data_with_timestamp.split(": ", 1)
try:
    # 解码AIS数据
    decoded_msg = decode(ais_data)
    # 打印解码后的动态信息，包括时间戳
    print("解码后的动态信息：")
    print(f"MMSI: {decoded_msg.mmsi}")
    print(f"纬度: {decoded_msg.lat}")
    print(f"经度: {decoded_msg.lon}")
    print(f"速度: {decoded_msg.speed}")
    print(f"航向: {decoded_msg.heading}")
    print(f"时间戳: {timestamp}")
except Exception as e:
    print(f"解码失败: {e}")