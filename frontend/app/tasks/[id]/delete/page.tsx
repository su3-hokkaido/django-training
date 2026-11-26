import Link from "next/link";
import DeleteTaskForm from "../../../_components/DeleteTaskForm";
import { getTask } from "../../../_lib/server";

export default async function TaskDeletePage({ params }: { params: Promise<{ id: string }> }) {
  const task = await getTask((await params).id);

  return (
    <>
      <h1>ToDo Task Deletion Confirmation!!!</h1>
      <Link href="/">タスク一覧へ戻る</Link>
      <DeleteTaskForm task={task} />
    </>
  );
}
