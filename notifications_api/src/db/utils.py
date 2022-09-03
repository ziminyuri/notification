from db.rabbitmq_producer import RabbitMQProducer, get_rabbitmq_producer


def init_queues(
    queues_list: list[str],
    mq_producer: RabbitMQProducer = get_rabbitmq_producer(),
) -> None:
    for queue in queues_list:
        mq_producer.create_queue(queue)
