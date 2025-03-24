import grpc
import homework_pb2
import homework_pb2_grpc
import queue
import numpy as np

if __name__ == "__main__":
    channel = grpc.insecure_channel("andromeda.fi.muni.cz:58110")
    stub = homework_pb2_grpc.HomeworkStub(channel)
    data = homework_pb2.BeginData(email="567769@mail.muni.cz")
    response = stub.Begin(data)
    token = response.token

    print("TOKEN:", token)

    print("PART 1")
    print("info:", response.info)

    print("PART 2")
    result = response.adderTask.a + response.adderTask.b
    data = homework_pb2.AdderTaskResponse(token=token, result=result)
    response = stub.Adder(data)

    print("info:", response.info)

    matrix = np.array([row.values for row in response.matrixTask.rows])
    determinant = round(np.linalg.det(matrix))
    data = homework_pb2.MatrixTaskResponse(token=token, determinant=determinant)
    response = stub.Matrix(data)

    print("PART 3")
    print("info:", response.info)

    send_queue = queue.SimpleQueue()
    data = homework_pb2.FlipLineRequest(token=token)
    response = stub.ReadLine(data)

    for point in response:
        new_point = homework_pb2.Point(x=point.y, y=point.x)
        send_queue.put(homework_pb2.FlipLineResponse(token=token, point=new_point))
    send_queue.put(None)
    response = stub.SendLine(iter(send_queue.get, None))

    print("PART 4")
    print("info:", response.info)
