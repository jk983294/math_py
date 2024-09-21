import pyarrow as pa
import pyarrow.parquet as pq
import pyarrow.compute as pc

if __name__ == '__main__':
    data = [pa.array([1, 2, 3, 4]), pa.array(['foo', 'bar', 'baz', None]), pa.array([True, None, False, True])]
    batch = pa.RecordBatch.from_arrays(data, ['f0', 'f1', 'f2'])
    batches = [batch] * 5
    table = pa.Table.from_batches(batches)
    tables = [table] * 2
    table_all = pa.concat_tables(tables)
    print(table_all)
    print(table_all.num_rows)

    c = table_all[0]  # columns are instances of ChunkedArray
    print(c.num_chunks)
    print(c.chunk(0))  # [1, 2, 3, 4]

    df = c.to_pandas()
    print(df)
