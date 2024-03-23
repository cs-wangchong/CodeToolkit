public class Test1 {
    public InputStream getAttachmentInputStream(final String attachmentId) throws MessagingException {
        return database.execute(false, new DbCallback<InputStream>() {
            @Override
            public InputStream doDbWork(final SQLiteDatabase db) throws WrappedException {
                Cursor cursor = db.query("message_parts",
                        new String[] { "data_location", "data", "encoding" },
                        "id = ?",
                        new String[] { attachmentId },
                        null, null, null);
                try {
                    if (!cursor.moveToFirst()) {
                        return null;
                    }

                    int location = cursor.getInt(0);
                    String encoding = cursor.getString(2);

                    InputStream rawInputStream = getRawAttachmentInputStream(cursor, location, attachmentId);
                    return getDecodingInputStream(rawInputStream, encoding);
                } finally {
                    cursor.close();
                }
            }
        });
    }
}

