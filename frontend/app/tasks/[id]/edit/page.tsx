import Link from "next/link";
import TaskForm from "../../../_components/TaskForm";
import { getMe, getTask } from "../../../_lib/server";

export default async function TaskEditPage({ params }: { params: Promise<{ id: string }> }) {
  const { id } = await params;
  const [me, task] = await Promise.all([getMe(), getTask(id)]);

  return (
    <>
      <h1>ToDo Edit!!!</h1>
      <Link href="/">タスク一覧へ戻る</Link>
      <p>
        <b>Current User is {me.username}</b>
      </p>
      <TaskForm key={task.id} task={task} />
    </>
  );
}
