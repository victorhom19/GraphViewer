from server.java.java_ast import get_ast

if __name__ == '__main__':
    code1 = """
    public class A extends B {
        @Override
        public void upsert(BaseEntry<MemorySegment> entry) {
            State currentState = state;
    
            lock.readLock().lock();
            try {
                currentState.memory.put(entry);
            } finally {
                lock.readLock().unlock();
            }
    
            try {
                if (currentState.memory.getBytesSize() >= config.flushThresholdBytes()) {
                    flush();
                }
            } catch (IOException e) {
                throw new UncheckedIOException(e);
            }
        }
    }
    """
    code2 = """
        class Example{
            public static void main(){
                int a;
                a = 5;
            }
        }
    """
    print(code2)
    print(get_ast(code2))
